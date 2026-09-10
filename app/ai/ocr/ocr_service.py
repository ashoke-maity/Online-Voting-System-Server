from paddleocr import PaddleOCR
import cv2
import re


# Load OCR model once when the application starts
ocr = PaddleOCR(
    use_textline_orientation=True,
    lang="en",
    enable_mkldnn=False
)


def extract_document_number(image_path: str, document_type: str):

    # Read image
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Unable to read the uploaded image.")

    # Run OCR
    prediction = ocr.predict(img)

    if not prediction:
        raise ValueError("No text detected in the document.")

    # Extract recognized text
    texts = prediction[0]["rec_texts"]
    all_text = " ".join(texts)

    # Normalize spaces
    all_text = re.sub(r"\s+", " ", all_text).strip()

    # Aadhaar
    if document_type == "AADHAAR":
        match = re.search(
            r"\d{4} \d{4} \d{4}",
            all_text
        )

    # Voter / EPIC
    elif document_type == "VOTER":
        match = re.search(
            r"\b[A-Z]{3}\d{7}\b"
            r"|\b[A-Z]{2,3}/\d{2,3}/\d{2,4}/\d{4,6}\b",
            all_text
        )

    # PAN
    elif document_type == "PAN":
        match = re.search(
            r"\b[A-Z]{5}\d{4}[A-Z]{1}\b",
            all_text
        )

    else:
        raise ValueError("Invalid document type.")

    if match:
        return {
            "document_number": match.group(),
            "extracted_text": all_text
        }

    return {
        "document_number": None,
        "extracted_text": all_text
    }