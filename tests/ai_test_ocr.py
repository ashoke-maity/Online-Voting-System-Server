from app.ai.ocr.ocr_service import extract_document_number


image_path = "ai_test/ashoke_aadhaar.jpg"

result = extract_document_number(
    image_path=image_path,
    document_type="AADHAAR"
)

print("\nOCR RESULT")
print("--------------------")
print("Document Number:", result["document_number"])
print("Extracted Text:", result["extracted_text"])