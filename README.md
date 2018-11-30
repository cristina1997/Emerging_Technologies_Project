# Emerging_Technologies_Project
***
## Run
First and foremost, you will need to install [Anaconda Version 3.7](https://www.anaconda.com/download/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (if not already installed).

1. **Clone Repo**

* Open your terminal/cmd in the folder you wish to download the repository and execute the following <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```> git clone https://github.com/cristina1997/Emerging_Technologies_Project.git```

2. **Run Notebook**

* Open your terminal/cmd in the project folder <br>
  * If you wish to run one of the notebook projects, once you have installed jupyter execute the following <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```> jupyter notebook```

3. **Run Python Script**

* Open your terminal/cmd in the project folder <br>
  1. Install libraries
    * First you need to go to the folder in which the script is <br>
    * Create a text file <br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```> touch requirements.txt``` <br>
    * Add the following to the text file <br>
      image==1.5.20 <br>
      numpy==1.14.3 <br>
      tensorflow==1.4.0 <br>
    * Now install the linbraries in the text file <br> 
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```> pip install -r requirements.txt``` <br>
  2. Resize images
    * Make sure you are in the same folder as your script <br>
    * If you're not then go to your command line and write <br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```> cd 4.Digit-Recognition-Scrip``` <br>
    * Next we need to resize ourimages <br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```> python resize-images.py``` <br>
  2. Run Script <br>
    * Now that everything is set up, you can finally run the script <br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```> python digit-recognition-script.py```

***

## Project Components
### 1. [Numpy random notebook](https://github.com/cristina1997/Emerging_Technologies_Project/blob/master/1.Numpy-Random-Notebook/numpy-random-notebook.ipynb)
A jupyter notebook I developed that explains the overall concept of the numpy.random package with plots from the four different distributions.

### 2. [Iris dataset notebook](https://github.com/cristina1997/Emerging_Technologies_Project/blob/master/2.Iris-Dataset-Notebook/iris-dataset-notebook.ipynb)
A jupyter notebook used to explain the iris dataset as well as the difficulty in separating the three species.

### 3. [MNIST dataset notebook](https://github.com/cristina1997/Emerging_Technologies_Project/blob/master/3.MNIST-Dataset-Notebook/MNIST-dataset-notebook.ipynb)
A jupyter notebook explaining how to read MNIST dataset.

### 4. [Digit recognition](https://github.com/cristina1997/Emerging_Technologies_Project/tree/master/4.Digit-Recognition-Script)
A Pythom script that takes an image of a handwritten number and uses super-vised-learning algorithm to recognise the digit.

### 5. [Digit recognition explained](https://github.com/cristina1997/Emerging_Technologies_Project/blob/master/5.Digit-Recognition-Notebook/digit-recognition-notebook.ipynb)
A jupyter notebook explaining the Digit Recognition Script implementation.
