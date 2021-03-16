#нужно сделать возможность добавления второго автора, можно сделать при помощи
#использования второго шаблона и выбора из двух при запуске программы?????????
from docxtpl import DocxTemplate
#замени на ввод из окон программы
doc = DocxTemplate("title_page_template.docx")
context = { 'UDK' : '335.72',
            'PROJECTNAME_RU' : 'СТАНДАРТ ВИРТУАЛЬНОГО (ON-LINE) АУДИТА СЕРВИСНОГО ЦЕНТРА ПО ОБСЛУЖИВАНИЯ ПРОДУКЦИИ У ПОТРЕБИТЕЛЕЙ',
            'NAME_RU': 'Антонов А.В.',
            'ADRESS_RU': 'Акционерное общество «Концерн военно-космической обороны «Алмаз-Антей» (Концерн ВКО «Алмаз-Антей»), Российская Федерация, 121471, г. Москва, ул. Верейская, д. 41',
            'email': '603083@gmail.com',
            'annotation_RU' : 'Представлен процессный подход к аудиту предприятием-изготовителем/поставщиком деятельности по сохранению качества выпускаемой продукции у потребителя на основе применения цифровых информационных технологий. Гарантией получения объективных, достоверных и воспроизводимых результатов виртуального (on-line) является стандарт на процесс аудита. Предложена модель системы виртуального (on-line) аудита деятельности по сохранению качества выпускаемой продукции у потребителя. Разработаны требования к содержанию стандартизованной процедуры виртуального (on-line) аудита.',
            'keywords_RU' : 'виртуальный (on-line) аудит, стандартизованная процедура, система сохранения качества продукции, управление компетентностью персонала',
            'PROJECTNAME_EN' : 'STANDARD VIRTUAL (ON-LINE) AUDIT OF THE PRODUCT SERVICE CENTRE AT CLIENTS',
            'NAME_EN' : 'Antonov A.V.',
            'ADRESS_EN' : 'Joint Stock Company "Concern of Military and Space Defence "Almaz-Antey" (Concern EKO "Almaz-Antey"), Russian Federation, 121471, Moscow, 41 Vereyskaya str',
            'annotation_EN' : 'A process approach to the audit by the manufacturer/supplier of activities aimed at preserving the quality of products at the consumer based on the application of digital information technologies is presented. The guarantee of obtaining objective, reliable and reproducible virtual (on-line) results is the standard for the audit process. A model of the system of virtual (on-line) audit of activity on preservation of quality of let out production at the consumer is offered. The requirements for the content of a standardized virtual (on-line) audit procedure have been developed.',
            'keywords_EN' : 'virtual (on-line) audit, standardized procedure, product quality assurance system, personnel competence management'}
doc.render(context)
doc.save("title_page.docx")