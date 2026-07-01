from DB.repository import DocumentRepository
from datetime import datetime
from Core.filemanager import FileManager
from Core.Thumbnails import ThumbnailGenerator
from Core.reader import PDFReader
from Core.models import Document

class DocumentServices:
    def __init__(self):
       self.repo = DocumentRepository()
       self.filemanager = FileManager()
       self.thumbnail_generator = ThumbnailGenerator()
       self.reader = PDFReader()

    def uploaded_document(self,uploaded_file,tags,description,lecture_date=None):

        # 1. Save file
        file_path = self.filemanager.save_file(uploaded_file)
        # 2. Generate thumbnail  
        thumbnail_path = self.thumbnail_generator.generate_thumbnail(file_path)
        # 3. Get total pages
        total_pages = self.thumbnail_generator.get_total_pages(file_path)
        # 4. Convert to images
        self.reader.pdf_to_images(file_path)
        # 5. create required variables : upload date
        upload_date = datetime.now().strftime("%Y-%m-%d")

        doc = Document(
            id=None,
            name=uploaded_file.name,
            path=file_path,
            thumbnail_path=thumbnail_path,
            tags=tags,
            description=description,
            upload_date=datetime.now().strftime("%Y-%m-%d"),
            lecture_date=lecture_date,
            total_pages=total_pages
        )

        # 6. Save to db
        self.repo.add_document(doc)
    
    def search_documents(self, tag=None, date=None):
        return self.repo.search_documents(tag, date)
    
    def get_all_documents(self):
        return self.repo.get_all_documents()
    
