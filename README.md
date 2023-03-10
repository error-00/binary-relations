# binary-relations
This project implements the binary relation method using the Python programming language and the Flask framework. A web application is created in which the user enters the number of objects to compare, their names, and fills in the pair relationship matrix. And finally gets the result.

The user enters the number of objects on the main page, and their names on the next page. The names must be unique, so if the user tries to enter the same names, the web application will throw an error and the user will have to enter different names for the objects.
Next, the user fills in the pairwise comparison matrix, but only for the upper triangular part. The rest of the matrix will be filled automatically based on the principle of symmetry.
In the matrix, as mentioned earlier, you can enter only three values: -1, 0, 1. This is to reflect the relative attractiveness of objects. If the user enters other values, the application will indicate this error to the user.
The results of the comparisons will be reduced to a matrix of comparisons, which will be displayed on the result page. On the same page, the order of ranking, ranking using relations, formal marks (for convenient display of transitivity check), transitivity check and conclusion will be displayed.
