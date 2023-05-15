# binary-relations
This project implements the binary relation method using the Python programming language and the Flask framework. A web application is created in which the user enters the number of objects to compare, their names, and fills in the pair relationship matrix. And finally gets the result.

The user enters the number of objects on the main page, and their names on the next page. The names must be unique, so if the user tries to enter the same names, the web application will throw an error and the user will have to enter different names for the objects. Next, the user fills in the pairwise comparison matrix, but only for the upper triangular part. The rest of the matrix will be filled automatically based on the principle of symmetry. In the matrix, as mentioned earlier, you can enter only three values: -1, 0, 1. This is to reflect the relative attractiveness of objects. If the user enters other values, the application will indicate this error to the user. The results of the comparisons will be reduced to a matrix of comparisons, which will be displayed on the result page. On the same page, the order of ranking, ranking using relations, formal marks (for convenient display of transitivity check), transitivity check and conclusion will be displayed.

Web-app completed in Ukrainian.

Main page:
![image](https://user-images.githubusercontent.com/90632114/224697300-989dc26a-ad5c-4b38-a3ee-d32a7efd5abc.png)
On this page user enters the number of objects. User can enter minimum 3. Else, program will not allow the user to move to the next page.

Enter name of object:
![image](https://user-images.githubusercontent.com/90632114/224697761-eda2b4af-8554-426e-bcae-ba577def0a93.png)
On this page user enters the names of objects. Names will be unique, else program will not allow the user to move to the next page.

Enter matrix:
![image](https://user-images.githubusercontent.com/90632114/224698156-d053fe68-89a9-44ee-a399-21927446fd2d.png)
On this page user fills the matrix. But, user fills only upper triangular part. The rest of the matrix will be filled automatically. User can enter only -1, 0, 1.

Page with result:
![image](https://user-images.githubusercontent.com/90632114/224698584-448a003a-492d-4ed7-9527-2b2e2d911cef.png)

![image](https://user-images.githubusercontent.com/90632114/224698636-22b1147a-b5ee-49e6-a4ae-b5f6d70d6e3f.png)

![image](https://user-images.githubusercontent.com/90632114/224698705-97b47b74-c93a-47c5-b484-222113e24a86.png)

On this page user can see results his work. First it is full matrix. Next ranging. Below conventions and later check for transitivity with conclusion.

