import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageDraw, ImageTk
from matplotlib import pyplot as plt
from tkinter import *
from tkinter.ttk import Entry
from tkinter import messagebox
from tkinter import filedialog
from PIL import *
from tkinter import ttk 



hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)

def Obrabotka():
    img = cv2.imread('books.jpg')

        # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels

    l2 = clahe.apply(l)  # apply CLAHE to the L-channel

    lab = cv2.merge((l2,a,b))  # merge channels
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
    cv2.imshow('Increased contrast', img2)
    cv2.imwrite('books.jpg', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Obrabotka1():
    img = cv2.imread('dounut.jpg')

        # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels

    l2 = clahe.apply(l)  # apply CLAHE to the L-channel

    lab = cv2.merge((l2,a,b))  # merge channels
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR

    cv2.imwrite('dounut2.jpg', img2)


def Aprox():

    fn = 'books.jpg' # имя файла, который будем анализировать
    img = cv2.imread(fn)

    hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    contours0, hierarchy = cv2.findContours( thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    #create an empty image for contours
    img_contours = np.uint8(np.zeros((img.shape[0],img.shape[1])))

    cv2.drawContours(img_contours, contours0, -1, (255,255,255), 1)

    cv2.imshow('origin', img) # выводим итоговое изображение в окно
    cv2.imshow('res', img_contours) # выводим итоговое изображение в окно

    cv2.waitKey()
    cv2.destroyAllWindows()

def Aprox_pr():

    fn = 'books.jpg' # имя файла, который будем анализировать
    img = cv2.imread(fn)

    hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    #thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    
    contours0, hierarchy = cv2.findContours( thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    #create an empty image for contours
    img_contours = np.uint8(np.zeros((img.shape[0],img.shape[1])))

    cv2.drawContours(img_contours, contours0, -1, (255,255,255), 1)

   # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv2.minAreaRect(cnt) # пытаемся вписать прямоугольник
        box = cv2.boxPoints(rect) # поиск четырех вершин прямоугольника
        box = np.int0(box) # округление координат
        area = int(rect[1][0]*rect[1][1]) # вычисление площади
        if area > 500:
            cv2.drawContours(img,[box],0,(255,0,0),2)

        

    cv2.imshow('contours', img) # вывод обработанного кадра в окно

    cv2.waitKey()
    cv2.destroyAllWindows()

def Aprox_el():

    Obrabotka1()
    fn = 'dounut2.jpg' # имя файла, который будем анализировать
    img = cv2.imread(fn)

    hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    contours0, hierarchy = cv2.findContours( thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    #create an empty image for contours
    img_contours = np.uint8(np.zeros((img.shape[0],img.shape[1])))

    cv2.drawContours(img_contours, contours0, -1, (255,255,255), 1)

   # перебираем все найденные контуры в цикле
    for cnt in contours0:
        if len(cnt)>4:
            ellipse = cv2.fitEllipse(cnt)
            cv2.ellipse(img,ellipse,(0,0,255),2)
        

        

    cv2.imshow('contours', img) # вывод обработанного кадра в окно

    cv2.waitKey()
    cv2.destroyAllWindows()




    

def Menu():
    window = Tk()

    #img = Image_()
    
    window.title("Menu")

    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200
    window.geometry('500x300+{}+{}'.format(w, h))
    window.configure(bg='#bb85f3')

  

    btn10 = Button(window, text="Обработка", padx=5, pady=5, command =Obrabotka , bg='#eec6ea')  
    btn10.pack(anchor="center", padx=20, pady=10)

   

    btn8 = Button(window, text="Аппроксимация", padx=5, pady=5, command =Aprox, bg='#eec6ea')  
    btn8.pack(anchor="center", padx=20, pady=10)

    btn9 = Button(window, text="Поиск прямоугольников", padx=5, pady=5, command =Aprox_pr , bg='#eec6ea')  
    btn9.pack(anchor="center", padx=20, pady=10)

    btn7 = Button(window, text="Поиск окружностей", padx=5, pady=5, command = Aprox_el, bg='#eec6ea')  
    btn7.pack(anchor="center", padx=20, pady=10)

    btn4 = Button(window, text="Выход", padx=5, pady=5, command = exit, bg='#eec6ea')  
    btn4.pack(anchor="center", padx=20, pady=10)

    window.mainloop()

Menu()