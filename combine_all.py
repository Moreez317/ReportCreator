from docxcompose.composer import Composer
from docx import Document as Document_compose
#filename_master - основной файл, который будет собран с остальными
#files_list - остальные файлы, их может быть множество
#отдельный прикол в том, что это говнецо не сбивает форматирование :)
def combine_all_docx(filename_master,files_list):
    number_of_sections=len(files_list)
    master = Document_compose(filename_master)
    composer = Composer(master)
    for i in range(0, number_of_sections):
        doc_temp = Document_compose(files_list[i])
        composer.append(doc_temp)
    composer.save("combined_file.docx")
filename_master="title_page.docx"
files_list=["main_part.docx"]
#можно добавить несколько файлов через запятую, прим. files_list=["main_part.docx", "another_one.docx"]
combine_all_docx(filename_master,files_list)
