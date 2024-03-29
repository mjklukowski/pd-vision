import cv2 as cv
import numpy as np
import math

def debug_time(name: str):
    def debug_time_decorator(func):
        def debug_time_wrapper(*args, **kwargs):
            self = args[0]
            e1 = cv.getTickCount()

            return_value = func(*args, **kwargs)

            e2 = cv.getTickCount()
            self.debug_data[name] = (e2 - e1)/ cv.getTickFrequency()

            return return_value
        return debug_time_wrapper
    return debug_time_decorator

class IAlgorithm:
    def _capture(self): pass
    def _preprocessing(self): pass
    def _segmentation(self): pass
    def _counting(self): pass
    def count(self) -> int: pass

class BaseAlgorithm(IAlgorithm):
    
    def __init__(self, img_path: str):
        self._img_path = img_path
        self.img_original_bgr = None
        self.count_result = None

        self.debug_data = {}

    def count(self) -> int:
        if self.count_result is not None:
            return self.count_result

        self._capture()
        self._preprocessing()
        self._segmentation()
        self._counting()
        return self.count_result

    @debug_time("execution_time_capture")
    def _capture(self):
        self.img_original_bgr = cv.imread(self._img_path)

        w = np.size(self.img_original_bgr, 1)
        h = np.size(self.img_original_bgr, 0)
        target_d = 1920 * 1080
        ratio = w / h

        target_h = math.sqrt(target_d * h / w)
        target_w = target_h * ratio

        target_h = math.ceil(target_h)
        target_w = math.ceil(target_w)

        self.img_original_bgr = cv.resize(self.img_original_bgr, (target_w, target_h))

class BaseBlobAlgorithm(BaseAlgorithm):

    @debug_time("execution_time_segmentation")
    def _segmentation(self):
        self._thresholding()
        self._morphology()
        self._extraction()

    def _thresholding(self): pass
    def _morphology(self): pass
    def _extraction(self): pass

    def _opening_closing(self, img, open_ksize: tuple = (3, 3), close_ksize: tuple = (17, 17), open_iterations=1, close_iterations=1):
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, open_ksize)
        img_opened = cv.morphologyEx(img, cv.MORPH_OPEN, kernel, iterations=open_iterations)

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, close_ksize)
        img_closed = cv.morphologyEx(img_opened, cv.MORPH_CLOSE, kernel, iterations=close_iterations)

        return img_closed
    
    def _closing_opening(self, img, close_ksize: tuple = (16, 16), open_ksize: tuple = (5, 5), close_iterations=1, open_iterations=1):
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, close_ksize)
        img_closed = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel, iterations=close_iterations)

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, open_ksize)
        img_opened = cv.morphologyEx(img_closed, cv.MORPH_OPEN, kernel, iterations=open_iterations)

        return img_opened

class BaseHsvBlobAlgorithm(BaseBlobAlgorithm):

    def __init__(self, img_path: str):
        super().__init__(img_path)
        self.img_prep_bgr = None
        self.img_prep_hsv = None
        self.img_prep_h, self.img_prep_s, self.img_prep_v = (None, None, None)
        self.img_h_thresh, self.img_s_thresh, self.img_v_thresh = (None, None, None)
        self.img_bitwise = None
        self.img_morphed = None
        self.blobs = None
        self.valid_blobs = None

        self._label_connectivity = 8
        self.min_blob_size = 500

    @debug_time("execution_time_preprocessing")
    def _preprocessing(self):
        self.img_prep_bgr = np.copy(self.img_original_bgr)

        self.img_prep_bgr = self._bluring(self.img_prep_bgr)
        self.img_prep_bgr = self._sharpening(self.img_prep_bgr)

    def _thresholding(self):
        self.img_prep_hsv = cv.cvtColor(self.img_prep_bgr, cv.COLOR_BGR2HSV)
        self.img_prep_h, self.img_prep_s, self.img_prep_v = cv.split(self.img_prep_hsv)

    @debug_time("execution_time_morphology")
    def _morphology(self):
        img_sv_thresh = cv.bitwise_and(self.img_s_thresh, self.img_v_thresh)
        self.img_bitwise = img_sv_thresh
        self.img_morphed = self._opening_closing(img_sv_thresh)

    @debug_time("execution_time_extraction")
    def _extraction(self):
        _, _, stats, centroids = cv.connectedComponentsWithStats(self.img_morphed, connectivity=self._label_connectivity)
        self.labels = [{ "stats": stats[i], "centroids": centroids[i]} for i in range(1, len(stats))]
        self.blobs, hierarchy = cv.findContours(self.img_morphed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    @debug_time("execution_time_counting")
    def _counting(self):
        self.count_result = 0
        self.valid_blobs = []

        self.debug_data["blob_count"] = len(self.labels)

        for label in self.labels:
            size = label["stats"][cv.CC_STAT_AREA]
            if size >= self.min_blob_size:
                self.valid_blobs.append(label)
                self.count_result += 1

    def _bluring(self, img, median_blur_ksize: int = 3, blur_ksize: tuple = (3, 3)):
        if median_blur_ksize is not None:
            img_blur = cv.medianBlur(img, median_blur_ksize)
        if blur_ksize is not None:
            img_blur = cv.blur(img_blur, blur_ksize)
        return img_blur

    def _sharpening(self, img, kernel=None):
        if kernel is None:
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        img_sharp = cv.filter2D(img, -1, kernel)
        return img_sharp