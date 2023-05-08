from tkinter import *
from tkinter import font 
from tkinter import scrolledtext, messagebox, filedialog 


window = Tk()
window.configure(bg="#928f8f")
window.geometry('500x600')
window.title('مدیریت')
color="#928f8f"
window.resizable(width=False, height=False)


lbl = Label(window, text='به نرم افزار مدیریتی سینا خوش آمدید ', font=('B Titr', 15),foreground="dark red",bg="#928f8f")
lbl.pack(side=TOP, pady=5, padx=0)

lable = Label(window, text='فرم ثبت نام', font=('B Nazanin Bold', 20),foreground="light green",bg="#928f8f")
lable.pack(side=TOP, pady=10, padx=0)
#====================================== text boxes and lables and variables =======================================
num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
scores=[ 20 , 12.5, 16,14,20,20,19,19.5 ,17,15]
classes=["ریاضی 1" ,"ریاضی 2","فیزیک 1","فیزیک 2","زبان تخصصی","اندیشه اسلامی","ادبیات فارسی","ساختمان داده ها","مدار های منطقی","طراحی زبان های برنامه سازی" ]
name=["هادی صدیق","سينا فلکي","مهدی شادرو","اکرم امانی","سید مجتبی طباطبایی","اشرف دادگر","فرزانه سادات موسوی","محمد کشاورز","احمد سلطانی","مجید شریعت طلب"]
ostad=["رضا بابایی","محمد مرادی","محمدرضا مصلایی","مهدی باباخانی","امیر میرحسینی","هوشنگ انصاری","علی منصف شکری","عزت الله مشفق","مهرداد عباسپور","سامان سلامیان"]
password=["24",24]


label1 = Label(window,font=('B Nazanin', 15), text=': نام ', bg=color)
label1.pack(side=TOP , pady=10, padx=145)

txt1 = Entry(window, width=30, borderwidth =5 , font= ('B Nazanin', 15),justify="right")
txt1.pack(side=TOP)



label2 = Label(window,font=('B Nazanin', 15), text=': نام خانوادگی ', bg=color)
label2.pack(side=TOP , pady=10, padx=145)

txt2 = Entry(window, width=30, borderwidth =5 , font= ('B Nazanin', 15),justify="right")
txt2.pack(side=TOP)



label3 = Label(window,font=('B Nazanin', 15), text=': پسورد ', bg=color)
label3.pack(side=TOP , pady=10, padx=145)

txt3 = Entry(window, width=30, borderwidth =5 , font= ('B Nazanin', 15),justify="right")
txt3.pack(side=TOP)

lable4 = Label(window, text='.چناچه قبلا ثبت نام کرده اید ، بر روی دکمه ورود کلیک کنید', font=('B Mehr', 12),foreground="yellow",bg="#928f8f")
lable4.pack(side=TOP, pady=5, padx=0)


#=================================================  دکمه ها  ====================================================

#زدن دکمه ی ثبت نام و ثبت شدن
def submit():
             num1=(txt1.get())
             num2=(txt2.get())
             num3=(txt3.get())
             operator= ""
            
             if num1 and num2 and num3 != operator :
                 name.append(f"{num1} {num2}")
                 password.append(num3)
                 messagebox.showinfo("پیغام",".حساب شما با موفقیت به ثبت رسید")
             else:
                  messagebox.showinfo("پیغام","لطفا همه موارد را مقدار دهی کنید و سپس ثبت کنید")
      

btn = Button(window, text='ثبت نام' ,width=7, borderwidth=7, font= ('B Nazanin Bold', 13) , command  =submit)
btn.pack(side=RIGHT , pady=40, padx=75)



#زدن دکمه ورود و باز شدن صفحه دوم
def Begin():
         
         window.destroy()


        
         page = Tk()
         page.configure(bg="#928f8f")
         page.geometry('500x600')
         page.title('مدیریت')
         page.resizable(width=False, height=False)
         color="#928f8f"
         
        
         menu1 = Menu(page) 
         menu1.add_cascade(label="بستن برنامه"  ,   command= page.destroy)
         page.config(menu=menu)
        
        
         lbl = Label(page, text='ورود مجدد شما را خوش آمد عرض میکنیم', font=('B Titr', 15),foreground="yellow",bg="#928f8f")
         lbl.pack(side=TOP, pady=5, padx=0)
         
         lable = Label(page, text='فرم ورود', font=('B Nazanin Bold', 20),foreground="green",bg="#928f8f")
         lable.pack(side=TOP, pady=10, padx=0)
        
         label1 = Label(page,font=('B Nazanin', 15), text=': نام ', bg=color)
         label1.pack(side=TOP , pady=10, padx=145)
        
         text1 = Entry(page, width=30, borderwidth =5 , font= ('B Nazanin', 15),justify="right")
         text1.pack(side=TOP)
         
         
         
         label2 = Label(page,font=('B Nazanin', 15), text=': نام خانوادگی ', bg=color)
         label2.pack(side=TOP , pady=10, padx=145)
         
         text2 = Entry(page, width=30, borderwidth =5 , font= ('B Nazanin', 15),justify="right")
         text2.pack(side=TOP)
         
         
         
         label3 = Label(page,font=('B Nazanin', 15), text=': پسورد ', bg=color)
         label3.pack(side=TOP , pady=10, padx=145)
         
         text3 = Entry(page, width=30, borderwidth =5 , font= ('B Nazanin', 15),justify="right")
         text3.pack(side=TOP)


         




         def submit2():
               num1=(text1.get())
               num2=(text2.get())
               num3=(text3.get())
               operator= ""
                 
               if num1 and num2 and num3 != operator :
                   #==================================== شرط ادمین بودن  ================================
                   if num1 and num2 and num3 == "admin" :
                      page.destroy()
                      page2 = Tk()
                      color="#928f8f"
                      page2.configure(bg=color)
                      page2.geometry('900x470')
                      page2.title('مدیریت')
                      page2.resizable(width=False, height=False)
                      lbl = Label(page2, text='به پنل سامانه مدیریتی سینا خوش آمدید', font=('B Mehr', 15),foreground="#FFF200",bg=color)
                      lbl.place(x="280" , y="7")
                      lbl2 = Label(page2, text="پنل ادمین", font=('B Titr', 20),foreground="green",bg=color)
                      lbl2.place(x="730" , y="7")
       

                      text_area = scrolledtext.ScrolledText(page2, width=65, height=20,bd=20)
                      text_area.pack(side=LEFT , pady=50, padx=100)
                      text_area.insert(INSERT, '\n\n\n             ....لطفا عملیات مدنظر خود را انتخاب نمائید')
                      text_area.insert(INSERT, "\n\n      =======================================================\n")
                      text_area.insert(INSERT, """                                                             
                                                                                                 (_)            
                                                                                            ___ _ _ __   __ _ 
                                                                                           / __| | '_ \ / _` |
                                                                                           \__ \ | | | | (_| |
                                                                                           |___/_|_| |_|\__,_|
                                                                                                                """)

                      
                      def karbaran():
                            text_area.delete(1.0,END)
                            text_area.insert(INSERT, "\n\n      ==================== لیست کاربران ===================\n")
                            text_area.insert(INSERT, " ")
                            for i in range(len(name)):
                                 text_area.insert(INSERT, f"     {i+1:2} : {  name[i]:7}  \n ")

                      btn1 = Button(page2, width=11, height=1, bd=8, fg='black',font=('B Mehr Bold', 12),  text='لیست کاربران',foreground="white",bg="#717171" ,command=karbaran )
                      btn1.place(x="700",y="90")          
                      
                      def kelas():
                            text_area.delete(1.0,END)
                            text_area.insert(INSERT, "\n\n      ==================== مشاهده کلاس ها ===================\n")
                            text_area.insert(INSERT, " ")
                            for i in range(len(classes)):
                                 text_area.insert(INSERT, f"     {i+1:2} : {  classes[i]:7}  \n ")

                      btn2 = Button(page2, width=11, height=1, bd=8, fg='black', font=('B Mehr Bold', 12), text='مشاهده کلاس ها',foreground="white",bg="#717171",command=kelas)
                      btn2.place(x="700",y="190")
                      
                      def asatid():
                            text_area.delete(1.0,END)
                            text_area.insert(INSERT, "\n\n      ==================== مشاهده لیست اساتید ================\n")
                            text_area.insert(INSERT, " ")
                            for i in range(len(ostad)):
                                 text_area.insert(INSERT, f"     {i+1:2} : {  ostad[i]:7}  \n ")

                      btn3 = Button(page2, width=11, height=1, bd=8, fg='black', font=('B Mehr', 12), text='مشاهده لیست اساتید',foreground="white",bg="#717171",command=asatid)
                      btn3.place(x="700",y="290")


                      

                      menu3 = Menu(page2) 
                      menu3.add_cascade(label="بستن برنامه"  ,   command= page2.destroy)
                      page2.config(menu=menu)
                      
                   

                   else:
                       
                        flag=0
                        flag2=0
                        NF=f"{num1} {num2}"
                        for i in range(len(password)):
                            if num3==password[i]:
                                flag+=1
                        for  i in range(len(name)):
                            if NF==name[i]:
                                flag2+=1
                        if flag and flag2 ==1 :
                             page.destroy()
                             page2 = Tk()
                             color="#928f8f"
                             page2.configure(bg=color)
                             page2.geometry('900x470')
                             page2.title('مدیریت')
                             page2.resizable(width=False, height=False)
                             lbl = Label(page2, text='به پنل کاربری سامانه مدیریتی سینا ، خوش آمدید', font=('B Mehr', 15),foreground="#FFDD00",bg=color)
                             lbl.place(x="265" , y="7")
                             lbl2 = Label(page2, text='نام : {}\n نام خانوادگی : {} \n رمز ورود : {}'.format(num1,num2,num3), font=('B Mehr', 15),foreground="#870231",bg=color)
                             lbl2.place(x="710" , y="275")
                             
                             
                             text_area = scrolledtext.ScrolledText(page2, width=65, height=20,bd=20)
                             text_area.pack(side=LEFT , pady=50, padx=100)
                             text_area.insert(INSERT, '\n\n\n             ....لطفا عملیات مدنظر خود را انتخاب نمائید')
                             text_area.insert(INSERT, "\n\n      =======================================================\n")
                             text_area.insert(INSERT, """                                                             
                                                                                                        (_)            
                                                                                                   ___ _ _ __   __ _ 
                                                                                                  / __| | '_ \ / _` |
                                                                                                  \__ \ | | | | (_| |
                                                                                                  |___/_|_| |_|\__,_|
                                                                                                                       """)
                             def nomre():
                                 text_area.delete(1.0,END)
                                 text_area.insert(INSERT, "\n\n      =========================== نمرات ========================\n")
                                 text_area.insert(INSERT, " ")
                                 for i in range(len(scores)):
                                      text_area.insert(INSERT, f"       {  classes[i]:7} : {scores[i]:5} \n ")
                             
                             btn1 = Button(page2, width=10, height=1, bd=8, fg='black',font=('B Mehr Bold', 12),  text='مشاهده ی نمرات',foreground="white",bg="#717171",command=nomre )
                             btn1.place(x="700",y="90")     
                             
                             def kelas():
                                 text_area.delete(1.0,END)
                                 text_area.insert(INSERT, "\n\n      ==================== مشاهده کلاس ها ===================\n")
                                 text_area.insert(INSERT, " ")
                                 for i in range(len(scores)):
                                      text_area.insert(INSERT, f"       {  classes[i]:7}  \n ")
                             
                             btn2 = Button(page2, width=10, height=1, bd=8, fg='black', font=('B Mehr Bold', 12), text='مشاهده کلاس ها',foreground="white",bg="#717171",command=kelas)
                             btn2.place(x="700",y="190")
                             menu3 = Menu(page2) 
                             menu3.add_cascade(label="بستن برنامه"  ,   command= page2.destroy)
                             page2.config(menu=menu)
                        else:
                            messagebox.showwarning("پیغام","شما در سیستم ثبت نام نکرده اید، لطفا اول ثبت نام نمایید")
                       
                       
                       
                       
                       
               else:
                     messagebox.showinfo("پیغام","لطفا همه موارد را مقدار دهی کنید و سپس ثبت کنید")


       
           

         btn = Button(page, text='ورود' ,width=15, borderwidth=7, font= ('B Nazanin Bold', 13), command=submit2)  
         btn.pack(side=TOP , pady=50, padx=100)
 





btn2 = Button(window, text='ورود' ,width=7, borderwidth=7, font= ('B Nazanin Bold',13), command=Begin  )  
btn2.pack(side=LEFT,pady=40, padx=75)



menu = Menu(window)
menu.add_cascade(label="بستن برنامه"  ,   command= window.destroy)
window.config(menu=menu)


  
window.mainloop()