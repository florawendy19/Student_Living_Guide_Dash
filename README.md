
# Student Living Guide Dash App

The Student Living Guide is a data visualization dashboard app (built on Dash) displaying crucial information about cost of Living indexes of countries and continents. This app is made for any student or anybody in New York city wishing to explore other parts of the world. It will give them support in deciding where to go depending on their bidget. 

## Table of Contents

  - [The App](#the-app)
  - [Motivation and Purpose](#https://github.com/UBC-MDS/Student_Living_Guide/blob/main/reports/proposal.md)
  - [Dashboard description](#dashboard-description)
  - [App Design](#app-design)
  - [If you want to help further develop the app](#if-you-want-to-help-further-develop-the-app)
  - [Contributing](#contributing)
  - [App Contributors](#app-contributors)
  - [License](#license)

## The App

You can access the dashboard app here: [Student Living App](https://spotify-explorer-pop.herokuapp.com/)

## Motivation and Purpose

Click [here ](#https://github.com/UBC-MDS/Student_Living_Guide/blob/main/reports/proposal.md) to read the full proposal of the project.

As international students, the main question that we all asked ourselves before moving to Vancouver was: How affordable is Vancouver city? How affordable a country or a city is, is indeed the biggest factor when it comes to choosing the country or city where one wants to pursue their studies. Many students, therefore, browse hundreds of websites to find indicators of the cost of living in the country or the city they plan to go to. However, this process can be exhaustive because the information about the cost of living is spread across different websites and the search results often contradict. How can we be sure that this process of comparing cities/countries based on the cost of living is less exhaustive for students and potentially yields reliable results? This is the question that our application `Student_Living_Guide` aims to address.

### User Persona

Quan is a 22-years old student pursuing an undergraduate degree in Neuroscience at New York University (NYU). After completing his freshman year at NYU, Quan is considering several student exchange programs abroad from his entire Sophomore year. Quan is hesitating between four countries which are: France, South Africa, India, and China. Aware that his one-year budget is limited, Quan decides to use the application `Student_Living_Guide` in order to make a choice that matches his budget. Through the `Student_Living_Guide` application, Quan will be able to interactively select those four countries and compare attributes such as rent/month, and groceries index.

The cost-of-living data on which the application `Student_Living_Guide` is based on New York as a reference point, therefore, the target market for our application is any student living in New York and who is considering other countries to pursue their studies. The `Student_Living_Guide` will guide them in making a more informed decision about the country they wish to pursue their studies.

### Usage

With the Student Living guide, student in New York desiring to pursue their studies elsewhere will be able to find the necessary information to comparing the living cost of any place with New York. Indeed, the can select any country from the list of countries to view the Cost of living displayed through the aid of a map as well as a density plot. Lastly, students can also select any two indices they wish to check the correlation which will be displayed in a scatter plot.

## Research questions and usage scenarios

Through our application, students in the shoes of our fictional character Quan will be able to answer the following questions:

- Which country has the highest cost of living?

- Which country has the lowest cost of living?

- What is the correlation between different indexes? For example, what is the correlation between the Groceries Index and Restaurant Price Index?

- Which country has the closest living cost compared to New York?

## Dashboard description

The app contains 3 tabs that shows a map, a stacked bar plot and a scatter chart
options for the plots.

- **Map** <br>

- **Stacked bar chart** <br>

- **Scatter chart** <br>


## App Design

<img width="919" src="./img/py-demo.gif">

## If you want to help further develop the app

1. Fork [the repository](https://github.com/UBC-MDS/spotify-explorer-py/)
2. Set up conda environment as follows

```bash
conda env create -f student_guide.yml
conda activate student_guide
```

3. To run the app locally, run the following command from the root of this repository

```python
python src/app.py
```

4. Create an issue on this repo to inform the owner about the changes/improvements you want to make. See **Contributing** section below for more details.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a [Code of Conduct](/CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## App Contributors

-Flora Wendmalgdo ouedraogo

## License

`Student_living_guide_dash` was created by Flora Ouedraogo. It is licensed under the terms of the [MIT License](main/LICENSE).
