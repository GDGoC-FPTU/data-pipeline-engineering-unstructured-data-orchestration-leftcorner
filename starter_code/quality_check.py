# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    """
    Kiểm tra chất lượng dữ liệu sau khi đã được chuẩn hóa.
    Trả về True nếu dữ liệu hợp lệ, False nếu không.
    """
    content = doc_dict.get("content", "")
    doc_id = doc_dict.get("document_id", "Unknown ID")

    # Check 1: Nội dung trống hoặc quá ngắn (< 10 ký tự)
    if not content or len(content.strip()) < 10:
        print(f"Watchman Alert: [Empty/Short Content] Document {doc_id} rejected.")
        return False

    # Check 2: Các từ khóa báo hiệu lỗi trích xuất (Semantic corruption)
    # Ví dụ: Lỗi OCR, lỗi hệ thống trích xuất...
    toxic_keywords = [
        "null pointer exception", 
        "error processing", 
        "corrupt", 
        "access denied",
        "invalid format",
        "failed to extract"
    ]
    
    content_lower = content.lower()
    for word in toxic_keywords:
        if word in content_lower:
            print(f"Watchman Alert: [Corrupt Content] Document {doc_id} contains toxic keyword: '{word}'")
            return False

    return True

