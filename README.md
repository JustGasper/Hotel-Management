# Hotel-Management
hotel program with database and graphical interface. Functions: To add, search and delete guests

In this folder you will find the Python code files, so that you can access the final program, which is called "Programa_Final". 
I want to clarify that all the files are in Spanish. Soon I will start sharing files in English. 

The program is constantly evolving. As I come up with new ideas and new improvements, I modify the code to make the program much more complete and professional.
For now, the program works perfectly. The only problem is that it does not update automatically. You have to close the program and reopen it again, so that specific data is updated. 




The file called "Huespedes" is basically in charge of searching for the person who is staying at the Hotel.
You have to enter as main data their name and last name or else, you can enter their National ID Card (Argentinean model DNI). Once you have entered it, the program will look for the guest's data in the database and will show them on the screen on some labels. 
It only shows you the person's information. For example: their name and last name, their check-in and check-out date, and other data that I consider valuable.


The file named "Eliminar_Huesped" is only responsible for deleting from the database all the information about the person that has been entered. 
Also, it changes a database value in the table "habitaciones" column "Disponible" and from the value "N" it changes it to "S" 
N = means that the room is NOT available 
S = means that the room IS available. 
Before deleting the person, ALL data will be displayed on the screen. Also, a pop-up window will be created, asking you if you are really sure to delete him/her. If you answer "Yes", it will delete all data automatically. If the answer is "No", no data will be deleted. 


The file called "Insertar_Huesped" is the most complete and, at the same time, the most complex of all. 
Its function is to add all the required information to the database. To do this, you will have to fill in all the blank boxes. 
All the boxes contain a checking system that verifies if the data entered is correct. If they are not, an alert message will be issued and ALL the information in that specific box will be deleted.  Otherwise, the program will continue to function normally until it has verified all the blanks, including the checkboxes. If everything is correct, a pop-up window will appear with a "successfully added guest" sign.
