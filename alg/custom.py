from . import *
from alg.ref import ReferenceAlgorithm

class CustomHsvBlobAlgorithm(ReferenceAlgorithm):

    def __init__(self, img_path):
        super().__init__(img_path)

        self.min_blob_size = math.ceil(math.pi * 7**2)
        self.safe_area = 0.8

    @debug_time("execution_time_preprocessing")
    def _preprocessing(self):

        # Blurring and sharpening
        super()._preprocessing()

        img_hsv = cv.cvtColor(self.img_prep_bgr, cv.COLOR_BGR2HSV)
        h, s, v = cv.split(img_hsv)

        # Contrast enhancement
        v_norm = cv.equalizeHist(v)

        # Lighting correction
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10))
        v_norm = cv.morphologyEx(v_norm, cv.MORPH_TOPHAT, kernel)

        self.img_prep_h = h
        self.img_prep_s = s
        self.img_prep_v = v_norm

        self.img_prep_hsv = cv.merge([h, s, v_norm])
        self.img_prep_bgr = cv.cvtColor(self.img_prep_hsv, cv.COLOR_HSV2BGR)

        # Apply preprocessing to all spaces (HSV -> BRG -> HSV)
        # hsv2bgr2hsv = self.img_prep_hsv = cv.cvtColor(self.img_prep_bgr, cv.COLOR_BGR2HSV)
        # self.img_prep_h, self.img_prep_s, self.img_prep_v = self.img_prep_h, self.img_prep_s, self.img_prep_v = cv.split(hsv2bgr2hsv)

    def _sharpening(self, img, kernel=None):
        return super()._sharpening(img, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))

    @debug_time("execution_time_thresholding")
    def _thresholding(self):
        # Apply color reduction
        self._color_reduction()
        self.img_h_thresh = self.h_mask

        # Threshold S space
        @debug_time("execution_time_thresholding_s")
        def thresholding_s(self):
            # Find S space threshold
            s_hist = self._get_single_channel_histogram(self.img_prep_s)

            mu = np.average(self.img_prep_s)
            sigma = np.abs(np.std(self.img_prep_s))

            # Threshold
            if mu <= 127:
                s_pix_val = np.ceil(mu + 1.5 * sigma)
                _, self.img_s_thresh = cv.threshold(self.img_prep_s, s_pix_val, 255, cv.THRESH_BINARY)
                self.debug_data["s_thresh_invert"] = False
            else:
                s_pix_val = np.ceil(mu - 1.5 * sigma)
                _, self.img_s_thresh = cv.threshold(self.img_prep_s, s_pix_val, 255, cv.THRESH_BINARY_INV)
                self.debug_data["s_thresh_invert"] = True

            self.img_s_thresh = cv.bitwise_and(self.img_s_thresh, self.h_mask)

            self.debug_data["s_thresh_level"] = s_pix_val

        thresholding_s(self)

        # Threshold V space
        @debug_time("execution_time_thresholding_v")
        def thresholding_v(self):
            # Noise removal
            img_v_blur = cv.GaussianBlur(self.img_prep_v, (3, 3), 0)

            # Constant V space threshold
            v_pix_val = 1

            _, self.img_v_thresh = cv.threshold(img_v_blur, v_pix_val, 255, cv.THRESH_BINARY)
            self.img_v_thresh = cv.bitwise_not(self.img_v_thresh)
            self.img_v_thresh = cv.bitwise_and(self.img_v_thresh, self.h_mask)

            self.debug_data["v_thresh_level"] = v_pix_val

        thresholding_v(self)

    @debug_time("execution_time_color_reduction")
    def _color_reduction(self):
        h = np.copy(self.img_prep_h)

        # Move all zeros to 179 (almost same red color)
        _, m = cv.threshold(h, 0, 179, cv.THRESH_BINARY_INV)
        h = cv.bitwise_or(h, m)

        # Remove most significant color
        h_threshed = self._reduce_colors(h)

        for i in range(0, 3):   # max 5; optimal 3
            h_threshed = self._reduce_colors(h_threshed)

        h_threshed = self._reduce_colors(h_threshed, close=True)

        mask = self._fill_holes(h_threshed)
        h_threshed = cv.bitwise_and(h, mask)

        _, self.h_mask = cv.threshold(h_threshed, 1, 255, cv.THRESH_BINARY)

    def _reduce_colors(self, img_h, close=False):
        img_hist = self._get_h_histogram(img_h)[1:]

        pix_val = img_hist.tolist().index(img_hist.max()) + 1
        mask = np.where(img_h == pix_val, 0, 255).astype("uint8")

        img_thresh = cv.bitwise_and(img_h, mask)

        if close:
            _, mask = cv.threshold(img_thresh, 0, 255, cv.THRESH_BINARY)
            mask = self._closing_opening(mask, close_ksize=(3, 3), open_ksize=(3, 3))
            img_thresh = cv.bitwise_and(img_h, mask)

        return img_thresh

    def _fill_holes(self, img_hollow):
        """Fill holes in binary image by finding all contours and filling them"""
        _, mask = cv.threshold(img_hollow, 0, 255, cv.THRESH_BINARY)
        cont, hier = cv.findContours(mask, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

        img_filled = mask
        for c in cont:
            cv.drawContours(img_filled, [c], 0, 255, -1)

        return img_filled

    def _get_single_channel_histogram(self, channel, bins=256):
        hist = cv.calcHist([channel], [0], None, [bins], [0,bins])
        hist = hist / hist.max()
        return hist

    def _get_h_histogram(self, h_channel):
        return self._get_single_channel_histogram(h_channel, 180)

    @debug_time("execution_time_morphology")
    def _morphology(self):

        # Sum S and V thresholds
        self.img_bitwise = cv.bitwise_or(self.img_s_thresh, self.img_v_thresh)

        # Remove small blobs
        sv_blobs = self._separate(self.img_bitwise)
        img_sv_morphed_big = np.copy(sv_blobs[0])

        # Closing and opening
        img_sv_morphed_big = self._closing_with_filling(img_sv_morphed_big, (17, 17))
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))
        img_sv_morphed_big = cv.morphologyEx(img_sv_morphed_big, cv.MORPH_OPEN, kernel, iterations=1)

        # Separate merged blobs
        while True:
            img_separated = self._separate_blobs(img_sv_morphed_big)
            if np.all(img_separated == img_sv_morphed_big):
                img_sv_morphed_big = img_separated
                break
            img_sv_morphed_big = img_separated

        # Apply safe area
        img_sv_morphed_big = self._remove_border_blobs(img_sv_morphed_big)

        self.img_morphed = img_sv_morphed_big

    def _separate(self, img):
        contours, hierarchy = cv.findContours(img, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
        areas = np.array([ cv.contourArea(c) for c in contours ])
        avg = np.average(areas)

        big_blobs = np.zeros_like(img)
        for c in contours:
            if cv.contourArea(c) > avg:
                cv.drawContours(big_blobs, [c], 0, 255, -1)

        small_blobs = img - big_blobs

        return (big_blobs, small_blobs)

    def _closing_with_filling(self, img, ksize=(3, 3)):
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, ksize)
        img = cv.morphologyEx(img, cv.MORPH_DILATE, kernel)
        img = self._fill_holes(img)
        return cv.morphologyEx(img, cv.MORPH_ERODE, kernel)

    @debug_time("execution_time_safe_area")
    def _remove_border_blobs(self, img_morphed):
        blobs, _ = cv.findContours(img_morphed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        img_height = np.size(img_morphed, 0)
        img_width = np.size(img_morphed, 1)
        offset_v = (1 - self.safe_area) * img_height / 2
        offset_h = (1 - self.safe_area) * img_width / 2

        for blob in blobs:
            moments = cv.moments(blob)

            if moments['m00'] > 0:
                cx = int(moments['m10']/moments['m00'])
                cy = int(moments['m01']/moments['m00'])

                if not ((cx < offset_h or cx > img_width - offset_h)
                        or (cy < offset_v or cy > img_height - offset_v)):
                    continue

            cv.drawContours(img_morphed, [blob], 0, 0, -1)

        return img_morphed

    @debug_time("execution_time_separation")
    def _separate_blobs(self, img_morphed):
        blobs, _ = cv.findContours(img_morphed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for blob in blobs:
            hull = cv.convexHull(blob)

            blob_area = float(cv.contourArea(blob))
            hull_area = cv.contourArea(hull)

            if hull_area == 0:
                solidity = 1
            else:
                solidity = blob_area / hull_area

            if solidity > 0.65:
                continue

            defect_points = self._get_convexity_defect_points(blob)

            if len(defect_points) < 2:
                continue

            blob_canvas = np.zeros_like(img_morphed)
            cv.drawContours(blob_canvas, [blob], 0, 255, -1)
            cv.drawContours(img_morphed, [blob], 0, 0, -1)

            for defect in defect_points:
                closest_defect = None
                min_d = np.inf
                for other_defect in defect_points:
                    if other_defect is defect:
                        continue

                    ax, ay = defect['coords']
                    bx, by = other_defect['coords']

                    d = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
                    if d < min_d:
                        min_d = d
                        closest_defect = other_defect

                if not closest_defect:
                    continue

                cv.line(blob_canvas, defect['coords'], closest_defect['coords'], [0, 0, 0])

            ksize = (7, 7)
            if blob_area < 1000:
                ksize = (5, 5)
            if blob_area < 500:
                ksize = (3, 3)

            kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, ksize)
            blob_canvas = cv.morphologyEx(blob_canvas, cv.MORPH_ERODE, kernel, iterations=1)

            img_morphed = cv.bitwise_or(img_morphed, blob_canvas)

        return img_morphed

    def _get_convexity_defect_points(self, blob):
        defect_points = []

        hull_indices = cv.convexHull(blob, returnPoints=False)
        try:
            defects = cv.convexityDefects(blob, hull_indices)

            for defect in defects:
                _, _, far_idx, d = defect[0]
                far = blob[far_idx][0]
                if d < 4250:
                    continue
                defect_points.append({
                    'coords': far,
                    'distance': d
                })
        finally:
            return defect_points