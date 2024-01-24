from BusinessLogic.Services.MaterialFileService import MaterialFileService
from Configuration.config import RELATIVE_PATH_TO_DATA_JSON
from DataAccess.Contexts.FileDataContext import FileDataContext
from DataAccess.Repositories.MaterialFileRepository import MaterialFileRepository
from Presentation.Controllers.MaterialController import MaterialController

def main():
    fileContext = FileDataContext(RELATIVE_PATH_TO_DATA_JSON)
    materialRepository = MaterialFileRepository(fileContext)
    materialService = MaterialFileService(materialRepository)
    materialController = MaterialController(materialService)

    material = Material("Brick", 300.0)
    print(materialController.add(material))
    print(materialController.get())
    material2 = Material("Slabs", 150.0)
    print(materialController.update(1, material2))
    print(materialController.get())

if __name__ == "__main__":
    main()


