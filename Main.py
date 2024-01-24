from BusinessLogic.Services.MaterialFileService import MaterialFileService
from Configuration.config import RELATIVE_PATH_TO_DATA_JSON
from DataAccess.Contexts.FileDataContext import FileDataContext
from DataAccess.Domains.Material import Material
from DataAccess.Repositories.MaterialFileRepository import MaterialFileRepository
from Presentation.Controllers.MaterialController import MaterialController

def main():
    fileContext = FileDataContext(RELATIVE_PATH_TO_DATA_JSON)
    materialRepository = MaterialFileRepository(fileContext)
    materialService = MaterialFileService(materialRepository)
    materialController = MaterialController(materialService)

if __name__ == "__main__":
    main()

# materialController.get()

materialController.add(Material("Brick", 200))
materialController.get_by_id(3)
