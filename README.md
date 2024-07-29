
# Tastopia
This Recipe Sharing Website is a web application developed with Django. This platform allows users to browse a variety of recipes, share their own culinary creations, and interact with other users. The website is structured to provide a seamless experience, from user registration to recipe management.



## Requirements:

- Python 3.x

- Django 4.x

- SQLite (or another database of your choice)

- Git (for version control)


## Installation

1. Clone the Repository:

```bash
  git clone https://github.com/Prangya2003/recipe-sharing-website.git
```

2. Navigate to the Project Directory:

```bash
  cd recipe-sharing-website/project
```    

3. Create a Virtual Environment (optional but recommended):

```bash
    python -m venv venv
```    

4. Activate the Virtual Environment:

- On Windows:
```bash
    .\venv\Scripts\activate
```  
- On macOS/Linux:
```bash
    source venv/bin/activate
```   

5. Install Dependencies:

```bash
  pip install -r requirements.txt
```   

6. Apply Migrations:

```bash
  python manage.py migrate
```   

7. Create a Superuser (optional for admin access):

```bash
  python manage.py createsuperuser
```   

8. Run the Development Server:

```bash
  python manage.py runserver
```   

9. Open Your Browser:
- Navigate to http://127.0.0.1:8000/ to view the website in action.

## Features

#### Landing Page 
- Welcoming page introducing the website and inviting users to sign up or log in.
####  Authentication
- Secure sign-up and login system to ensure personalized user access.
####  Home Page
- Displays a grid of recipe cards with previews. Users can click on these cards to view detailed recipe information.
####  Recipe Detail View
- Shows the full recipe, including ingredients and step-by-step instructions.
#### User Profile
- Allows users to view and manage their recipes, update their profile information,change their password and delete their account.
#### Save Recipe
- Users can save their favorite recipes for easy access later.
#### Search Feature
- Search recipes based on name, cuisine, and type of food (appetizer, main course,beverage, or dessert)
#### Ratings and Comments
- Users can rate recipes and leave comments to share their feedback.
#### Navbar
- Navigation links for Home, Profile, and Logout for easy site navigation.
#### Footer
- Includes links to FAQs, Contact Us, and Services for additional user support.

## Collaborators

- [@AkankshaBarik](https://github.com/AkankshaBarik): Developed the landing page,home page, footer and implemented commenting features.
- [@Prangya2003](https://www.github.com/prangya2003) : Handled CRUD operations for profiles and recipes, and designed the profile page.
- [@Silvasimran](https://github.com/Silvasim):  Created the save recipe functionality and search feature and implemented the rating feature.
