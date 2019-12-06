from Workers.Service import *
from Workers.Office import *
from Workers.Agrarian import *
from Workers.Administration import *
from Workers.HR import *
from Workers.Manager import *
import sqlite3
from Workers.WorkerAndFired import Worker
import inputANDoutput
con = sqlite3.connect("./Всі робітники.db")
cur = con.cursor()
data = Worker.main_data
fullname = "ЫФ фыв"
ID = 1
data_for_set = [fullname, ID]


class Main:
    con = sqlite3.connect("./Всі робітники.db")
    cur = con.cursor()

    def creator_of_classes(self):
        i = 0
        cur.execute('SELECT * FROM Всіробітники ')
        rows = cur.fetchall()
        try:
           for row in rows:
                first, last, father = row[1].split(" ")
                a = Worker.new_worker("{}.{}.{}.{}.{}.{}.{}.{}.{}".format(first, last, father,row[2],row[3], row[4], row[5], row[6], row[7]))
                inputANDoutput.InputAoutput.main_list.append(a)
                cur.execute('SELECT * FROM Землероби ')
                row1 = cur.fetchall()
                for row1n in row1:
                   if row1n[0] == row[0]:
                       ooo =  inputANDoutput.InputAoutput.main_list[i]
                       ooo.change_typework(Agrarian)
                   cur.execute('SELECT * FROM HR ')
                   row1 = cur.fetchall()
                   for row1n in row1:
                         if row1n[0] == row[0]:
                             ooo = inputANDoutput.InputAoutput.main_list[i]
                             ooo.change_typework(HR)
                cur.execute('SELECT * FROM Менеджери ')
                row1 = cur.fetchall()
                for row1n in row1:
                    if row1n[0] == row[0]:
                       ooo = inputANDoutput.InputAoutput.main_list[i]
                       ooo.change_typework(Manager)
                cur.execute('SELECT * FROM Обслуговуючийперсонал ')
                row1 = cur.fetchall()
                for row1n in row1:
                    if row1n[0] == row[0]:
                        ooo = inputANDoutput.InputAoutput.main_list[i]
                        ooo.change_typework(Service)
                cur.execute('SELECT * FROM Офісніробітники ')
                row1 = cur.fetchall()
                for row1n in row1:
                    if row1n[0] == row[0]:
                        ooo = inputANDoutput.InputAoutput.main_list[i]
                        ooo.change_typework(Office)
                cur.execute('SELECT * FROM Адміністрація ')
                row1 = cur.fetchall()
                for row1n in row1:
                    if row1n[0] == row[0]:
                        ooo = inputANDoutput.InputAoutput.main_list[i]
                        ooo.change_typework(Administrator)
                i = i + 1
        except:
            pass

    def save(self):
        con.commit()

    def close_DB(self):
        cur.close()
        con.close()

    def zvilnuty(self):
        cur.execute('UPDATE Всіробітники SET Статус = "Звільнено" WHERE ID = ?', [ID])


    #Worker

    def add_main_info_in_main(self):
        cur.execute('INSERT INTO Всіробітники VALUES(?, ?, ?, ?, ?, ?, ?, ?, "Працює")', data)

    def change_main_info_fullname(self):
        cur.execute('UPDATE Всіробітники SET ПІП= ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_rate(self):
        cur.execute('UPDATE Всіробітники SET Ставка = ? WHERE ID = ?', [data_for_set, ID] )

    def change_main_info_position(self):
        cur.execute('UPDATE Всіробітники SET Типроботи = ? WHERE ID = ?',[data_for_set, ID])

    def change_main_type_of_work(self):
        cur.execute('UPDATE Всіробітники SET Посада = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_insurance(self):
        cur.execute('UPDATE Всіробітники SET Медичнастраховка = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_military_ID(self):
        cur.execute('UPDATE Всіробітники SET Військовийквиток = ? WHERE ID = ?', [data_for_set, ID])



    # Manager
    def change_main_info_fullname_mng(self):
        cur.execute('UPDATE Менеджери SET ПІП= ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_rate_mng(self):
        cur.execute('UPDATE Менеджери SET Ставка= ? WHERE ID = ?',[data_for_set, ID])

    def change_main_info_position_mng(self):
        cur.execute('UPDATE Менеджери SET Типроботи = ? WHERE ID = ?',[data_for_set, ID])

    def change_main_type_of_work_mng(self):
        cur.execute('UPDATE Менеджери SET Посада = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_insurance_mng(self):
        cur.execute('UPDATE Менеджери SET Медичнастраховка = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_military_ID_mng(self):
        cur.execute('UPDATE Менеджери SET Військовийквиток = ? WHERE ID = ?', [data_for_set, ID])

    def add_main_info_in_manager(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO Менеджери VALUES(?, ?, ?, ?, ?, ?, ?, ?,  NULL, NULL)', data)

    def change_magr_duty_of_mgr(self):
        cur.execute("UPDATE Менеджери SET Обовязки = ? WHERE ID = ?",[data_for_set, ID] )

    def change_mng_subkject(self):
        cur.execute('UPDATE Менеджери SET Піддані = ? WHERE ID = ?',[data_for_set, ID])




    #HR

    def change_main_info_fullname_hr(self):
        cur.execute('UPDATE HR SET ПІП= ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_rate_hr(self):
        cur.execute('UPDATE HR SET Ставка = ? WHERE ID = ?',[data_for_set, ID] )

    def change_main_info_position_hr(self):
        cur.execute('UPDATE HR SET Типроботи = ? WHERE ID = ?',[data_for_set, ID])

    def change_main_type_of_work_hr(self):
        cur.execute('UPDATE HR SET Посада = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_insurance_hr(self):
        cur.execute('UPDATE HR SET Медична страховка = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_military_ID_hr(self):
        cur.execute('UPDATE HR SET Військовий квиток = ? WHERE ID = ?', [data_for_set, ID])

    def add_main_info_in_hr(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO HR VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL )', data)

    def change_hr_positions(self):
        cur.execute('UPDATE HR SET Посадинаякіопитує = ? WHERE ID = ?',[data_for_set, ID])

    def change_hr_for_whom(self):
        cur.execute('UPDATE HR SET Дляякихменеджерів = ? WHERE ID = ?',[data_for_set, ID] )

    def change_hr_duty_of_hr(self):
        cur.execute("UPDATE HR SET Обовязки = ? WHERE ID = ?",[data_for_set, ID])



    #Agrarian

    def change_main_info_fullname_agr(self):
        cur.execute('UPDATE Землероби SET ПІП= ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_rate_agr(self):
        cur.execute('UPDATE Землероби SET Ставка = ? WHERE ID = ?',[data_for_set, ID] )

    def change_main_info_position_agr(self):
        cur.execute('UPDATE Землероби SET Типроботи = ? WHERE ID = ?',[data_for_set, ID])


    def change_main_type_of_work_agr(self):
        cur.execute('UPDATE Землероби SET Посада = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_insurance_agr(self):
        cur.execute('UPDATE Землероби SET Медичнастраховка = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_military_ID_agr(self):
        cur.execute('UPDATE Землероби SET Військовийквиток = ? WHERE ID = ?', [data_for_set, ID])

    def add_main_info_in_agrararian(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO Землероби VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL)', data)

    def change_agr_chief(self):
        cur.execute('UPDATE Землероби SET Начальник = ? WHERE ID = ?',[data_for_set, ID]  )

    def change_agr_duty_agrar(self):
        cur.execute("UPDATE Землероби SET Обовязки = ? WHERE ID = ?",[data_for_set, ID] )

    def change_agr_tools(self):
        cur.execute('UPDATE Землероби SET Інструменти = ? WHERE ID = ?',[data_for_set, ID] )



    #Office

    def change_main_info_fullname_office(self):
        cur.execute('UPDATE Офісніробітники SET ПІП= ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_rate_office(self):
        cur.execute('UPDATE Офісніробітники SET Ставка = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_position_office(self):
        cur.execute('UPDATE Офісніробітники SET Типроботи = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_type_of_work_office(self):
        cur.execute('UPDATE Офісніробітники SET Посада = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_insurance_office(self):
        cur.execute('UPDATE Офісніробітники SET Медичнастраховка = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_military_ID_office(self):
        cur.execute('UPDATE Офісніробітники SET Військовийквиток = ? WHERE ID = ?', [data_for_set, ID])

    def add_main_info_in_office(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO Офісніробітники VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL)', data)

    def change_office_chief(self):
        cur.execute('UPDATE Офісніробітники SET Начальник = ? WHERE ID = ?',[data_for_set, ID] )

    def change_office_duty_office(self):
        cur.execute("UPDATE Офісніробітники SET Обовязки = ? WHERE ID = ?",[data_for_set, ID] )


    def change_office_unit(self):
        cur.execute("UPDATE Офісніробітники SET Підрозділ = ? WHERE ID = ?",[data_for_set, ID] )


    #Service

    def change_main_info_fullname_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET ПІП= ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_rate_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Ставка = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_position_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Типроботи = ? WHERE ID = ?', [data_for_set, ID])


    def change_main_type_of_work_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Посада = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_insurance_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Медичнастраховка = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_military_ID_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Військовийквиток = ? WHERE ID = ?', [data_for_set, ID])

    def add_main_info_in_service(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO Обслуговуючийперсонал VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL)', data)

    def change_service_chief(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Начальник = ? WHERE ID = ?', [data_for_set, ID] )



    def change_service_tools_of_service(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Інструменти = ? WHERE ID = ?',[data_for_set, ID] )

    def change_service_area(self):
        cur.execute('UPDATE Обслуговуючийперсонал SET Територія = ? WHERE ID = ?',[data_for_set, ID])



    #Administration

    def change_main_info_fullname_adm(self):
        cur.execute('UPDATE Адміністрація SET ПІП= ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_rate_adm(self):
        cur.execute('UPDATE Адміністрація SET Ставка = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_position_adm(self):
        cur.execute('UPDATE Адміністрація SET Типроботи = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_type_of_work_adm(self):
        cur.execute('UPDATE Адміністрація SET Посада = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_insurance_adm(self):
        cur.execute('UPDATE Адміністрація SET Медичнастраховка = ? WHERE ID = ?', [data_for_set, ID])

    def change_main_info_military_ID_adm(self):
        cur.execute('UPDATE Адміністрація SET Військовийквиток = ? WHERE ID = ?', [data_for_set, ID])

    def add_main_info_in_administation(self):
        self.add_main_info_in_main()
        cur.execute('INSERT INTO Адміністрація VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL, NULL)', data)

    def change_administation_chief(self):
        cur.execute('UPDATE Адміністрація SET Начальник = ? WHERE ID = ?',[data_for_set, ID] )

    def change_administation_duty_of_adm(self):
        cur.execute("UPDATE Адміністрація SET Обовязки = ? WHERE ID = ?",[data_for_set, ID] )


    def change_administation_monitor_of_unit(self):
        cur.execute('UPDATE Адміністрація SET Відповідальнийзапідрозділ = ? WHERE ID = ?', [data_for_set, ID])


    def change_administation_helper(self):
        cur.execute('UPDATE Адміністрація SET Помічник = ? WHERE ID = ?',[data_for_set, ID] )


    #Відображення даних

    def show_data_main(self):
        cur.execute("SELECT * FROM Всіробітники")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tПосада\t\tТип роботи\t\tМедична страховка\t\tВійськовий квиток\t\t\Статус")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8]))

    def show_data_adm(self):
        cur.execute("SELECT * FROM Адміністрація")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tПосада\t\tТип роботи\t\tМедична страховка\t\tВійськовий квиток\t\t\Начальник\t\tВідповідальний за підрозділ\t\tПомічник\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))

    def show_data_agr(self):
        cur.execute("SELECT * FROM Землероби")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tПосада\t\tТип роботи\t\tМедична страховка\t\tВійськовий квиток\t\t\Начальник\t\tІнструменти\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

    def show_data_hr(self):
        cur.execute("SELECT * FROM HR")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tПосада\t\tТип роботи\t\tМедична страховка\t\tВійськовий квиток\t\t\Посади, на які опитує\t\tДля яких менеджерів\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t\t\t\t\t{}\t\t\t\t\t\t\t\t{}\t\t\t\t\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

    def show_data_mng(self):
        cur.execute("SELECT * FROM Менеджери")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tПосада\t\tТип роботи\t\tМедична страховка\t\tВійськовий квиток\t\t\Піддані\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

    def show_data_office(self):
        cur.execute("SELECT * FROM Офісніробітники")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tПосада\t\tТип роботиt\tМедична страховка\t\tВійськовий квиток\t\t\Начальник\t\tПідрозділ\t\tОбов'язки")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

    def show_data_service(self):
        cur.execute("SELECT * FROM Обслуговуючийперсонал")
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tПосада\t\tТип роботи\t\tМедична страховка\t\tВійськовий квиток\t\t\Начальник\t\tІнструменти\t\tТериторія")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))



    #Фільтри пошуку

    def search_position(self):
        cur.execute("SELECT * FROM Всіробітники WHERE Типроботи = ?", [data_for_set])
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tПосада\t\tТип роботи\t\tМедична страховка\t\tВійськовий квиток")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7]))

    def search_PIP(self):
        cur.execute("SELECT * FROM Всіробітники WHERE ПІП = ?", [data_for_set])
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tПосада\t\tТип роботи\t\tМедична страховка\t\tВійськовий квиток")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7]))

    def search_id_global(self):
        cur.execute("SELECT * FROM Всіробітники WHERE ID = ?", [data_for_set])
        rows = cur.fetchall()
        print("id\t\tПІП\t\t\t\tСтать\t\tСтавка\t\tПосада\t\tТип роботи\t\tМедична страховка\t\tВійськовий квиток")
        for row in rows:
            print("{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7]))


Data_Base = Main()

