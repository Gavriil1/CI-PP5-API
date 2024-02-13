# Le NoteAPI in DRF

**Developer: Gavriil Spyropoulos**

💻 [Live link](https://ci-p5-project-api-part-500c148fe358.herokuapp.com/)

This repository contains the API set up using Django REST Framework for "Le Note" front-end application ([repository here](https://github.com/Gavriil1/CI-PP5-API) and [live website here](https://ci-p5-react-part-9d6b24103236.herokuapp.com/))

## Table of Contents
  - [User Stories](#user-stories)
  - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Validation](#validation)
  - [Testing](#testing)
  - [Credits](#credits)

## User Stories

The back-end section of the project focuses on its administration side and covers one user story:
- As an admin, I want to be able to create, edit and delete the users, notes, likes, feedback messages so that I can have a control over the content of the application and remove any potential inappropriate content


## Database

The following models were created to represent the database model structure of the application:
<img src="docs/readme/db.png">

#### User Model

- The User model contains information about the user. It is part of the Django allauth library.
- One-to-one relation with the Profile model owner field
- ForeignKey relation with the Notes model owner field
- ForeignKey relation with the Like model owner field

#### Profile Model

- The Profile model contains the following fields: id, owner, created_at, updated_at, name, content, image
- One-to-one relation between the owner field and the User model id field

#### Notes Model

- The Post model contains the following fields: id, owner, created_at, updated_at, title, content
- ForeignKey relation with the Like model post field

#### Like Model

- The Like model contains the following fields: id, owner, post and created_at
- ForeignKey relation between to the User model id field
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the post field and the Post model post field

##### Back to [top](#table-of-contents)


## Technologies Used

### Languages & Frameworks

- Python
- Django

### Libraries & Tools


- [Cloudinary](https://cloudinary.com/) to store static  files.
- [Dbdiagram.io](https://dbdiagram.io/home) used to create database diagram.
- [Git](https://git-scm.com/) was used for version control. The versions were pushed from gitpod to github.
- [GitHub](https://github.com/) The specified location served as a remote repository for storing project code.”
- [Gitpod)](https://gitpod.io/workspaces) - was used as IDE
- [Heroku](https://heroku.com) was used to deploy the project into live environment
- [Django REST Framework](https://www.django-rest-framework.org/) was used to develop backend API website.
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) was used as authentication plugin.
- [Pillow](https://pillow.readthedocs.io/en/stable/) was used for image processing and validation
- [Psycopg2](https://www.psycopg.org/docs/) was used as a PostgreSQL database adapter for Python
- [ElephantSQL](https://www.elephantsql.com/) – ElephantSQL was used during application development.

##### Back to [top](#table-of-contents)


## Validation

### PEP8 Validation
[PEP8](https://pep8ci.herokuapp.com/) Validation Service was used to check the code for PEP8 requirements. All the code passes with no errors or warnings.

In settings.py we have two long lines of code, which was not possible to make shorter:
158: E501 line too long (88 > 79 characters): 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
167: E501 line too long (80 > 79 characters): 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',


## Testing

The Manual test was carried out on the app:


### Manual testing of user stories

- As an admin, I want to be able to create, edit and delete the users, notes,and likes, so that I can have a control over the content of the application and remove any potential inappropriate content

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------
User | Create, update & delete user | A user can be created, edited or deleted | Works as expected
User | Change permissions | User permissions can be updated | Works as expected
Profile | Create, update & delete | User profile can be created, edited or deleted | Works as expected
Note | Create, update & delete | A post can be created, edited or deleted | Works as expected
Like | Create & delete | A like can be created or deleted (like / unlike post) | Works as expected
Feedback Message | Create & delete | A Feedback message can be created or deleted  | Works as expected


In addition, notes,  likes, feedback messages  can be created by logged-in users only. Users can only update or delete the content which was created by themselves.

<details><summary>Screenshots - USER</summary>
    <details><summary>Create user</summary>
    <img src="docs/user_story_testing/create_user_1_api_test.png">
    <img src="docs/user_story_testing/create_user_2_api_test.png">
    <img src="docs/user_story_testing/create_user_3_api_test.png">
    </details>
    <details><summary>Change user permissions</summary>
    <img src="docs/user_story_testing/update_user_api_test.png">
    </details>
</details>

<details><summary>Screenshots - PROFILE</summary>
    <details><summary>Update profile</summary>
    <img src="docs/user_story_testing/3-update-user-profile-1.png">
    <img src="docs/user_story_testing/3-update-user-profile-2.png">
    </details>
        <details><summary>Delete profile</summary>
    <img src="docs/user_story_testing/4-delete_user_profile_1.png">
    <img src="docs/user_story_testing/4-delete_user_profile_2.png">
    </details>
</details>

<details><summary>Screenshots - Notes</summary>
    <details><summary>Create note</summary>
    <img src="docs/user_story_testing/5_create_note_api_test_1.png">
    <img src="docs/user_story_testing/5_create_note_api_test_2.png">
    </details>
    <details><summary>Update note</summary>
    <img src="docs/user_story_testing/6_update_note_api_test_1.png">
    <img src="docs/user_story_testing/6_update_note_api_test_2.png">
    </details>
    <details><summary>Delete note</summary>
    <img src="docs/user_story_testing/7_delete_note_api_test_1.png">
    <img src="docs/user_story_testing/7_delete_note_api_test_2.png">
    </details>
</details>

<details><summary>Screenshots - LIKE</summary>
    <details><summary>Create like - like post</summary>
    <img src="docs/user_story_testing/8_create_like_api_test_1.png">
    <img src="docs/user_story_testing/8_create_like_api_test_2.png">
    </details>
    <details><summary>Delete like - unlike post</summary>
    <img src="docs/user_story_testing/9_delete_like_api_test_1.png">
    <img src="docs/user_story_testing/9_delete_like_api_test_2.png">
    </details>
</details>

<details><summary>Screenshots - Feedback Message</summary>
    <details><summary>Create Feedbac message</summary>
    <img src="docs/user_story_testing/10_create_feedback_api_test_1.png">
    <img src="docs/user_story_testing/10_create_feedback_api_test_2.png">
    </details>
    <details><summary>Delete Feedback Message</summary>
    <img src="docs/user_story_testing/11_delete_api_test_1.png">
    <img src="docs/user_story_testing/11_delete_api_test_2.png">
    <img src="docs/user_story_testing/11_delete_api_test_3.png">
    </details>
</details>




##### Back to [top](#table-of-contents)


## Credits

### Images

- The default user avatar image is taken from the Code Institute walkthrough.
- Website Logo was found on google.

### Code

This project was created based on the Code Institute's Django REST API walkthrough project ['Moments'](https://github.com/Code-Institute-Solutions/drf-api).

##### Back to [top](#table-of-contents)