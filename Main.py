from BusinessLogic.Services.MaterialFileService import MaterialFileService
from Configuration.config import RELATIVE_PATH_TO_DATA_JSON
from DataAccess.Contexts.FileDataContext import FileDataContext
from DataAccess.Domains.Material import Material
from DataAccess.Repositories.MaterialFileRepository import MaterialFileRepository
from Presentation.Controllers.MaterialController import MaterialController

fileContext = FileDataContext(RELATIVE_PATH_TO_DATA_JSON)
materialRepository = MaterialFileRepository(fileContext)
materialService = MaterialFileService(materialRepository)
materialController = MaterialController(materialService)

# materialController.get()
material = Material("Brick", 200.0)
materialController.add(material)
# print(materialController.get_by_id("3"))
