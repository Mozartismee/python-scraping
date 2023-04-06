This repository contains code samples for the book <a href="http://shop.oreilly.com/product/0636920078067.do">Web Scraping with Python 2nd Edition</a>, along with beginner-friendly explanations and figures to make the original code more readable.

In addition to providing clearer code samples, I have also connected this project to the GPT-4 API to enhance its functionality.

Feel free to ask any questions you may have about this book or web scraping in general!

| 物件                      | 功用                                                   | 目的                                                                                                    | 相關方法                                             |
|---------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| google.cloud.vision       | 實現與 Google Cloud Vision API 的交互                   | 為了使用 Vision API 進行 OCR，提取圖像中的文本                                                          | -                                                    |
| vision.ImageAnnotatorClient | Google Cloud Vision API 的客戶端                      | 通過這個客戶端，對每個圖像進行文本檢測和 OCR                                                              | `text_detection()`                                  |
| pdf2image                 | 將 PDF 文件轉換為圖像                                 | 為提供給 Vision API 以進行 OCR，先將 PDF 分割為多個頁面，並將這些頁面轉換為圖像格式（如 JPEG 格式）         | `convert_from_path()`                               |
| io.BytesIO                | 提供讀寫字節數組的二進制流對象                         | 將圖像保存為字節數組，以便在進行 OCR 時將其傳遞給 Vision API                                               | `getvalue()`, `save()`                              |
| vision.Image              | 代表要對其執行文本檢測的圖像                          | 使用從 PDF 轉換而來的圖像生成此物件，並將其提供給 Vision API 以進行 OCR                                   | -                                                    |
| response （API 響應物件）    | Vision API 文本檢測函數的結果                         | 存儲從圖像中檢測到的文本信息                                                                             | `text_annotations` 屬性                              |
| text_data （文本註釋）      | 紀錄檢測到的文本及其相關信息的物件列表                | 來自 Google Vision API 的帶有 OCR 文本結果的物件。包含檢測到的文本、位置經過排序的信息                 | `description` 屬性（用於獲取檢測到的文本）            |
