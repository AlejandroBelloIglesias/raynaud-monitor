# Summary

Hybrid app for patients with the [Síndrome Raynaud](https://es.wikipedia.org/wiki/Fen%C3%B3meno_de_Raynaud) that manifests under conditions of cold, stress and other minor circumstances such as smoking.

The app allows registering, viewing and modifying Raynaud episodes and their information including the possible triggers (cold, stress, smoking, etc.) as the affected body parts.

The goal is from monitoring and progress of the syndrome to the facilitation of information to prevent it or treat its symptoms as well as a statistical analysis of a centralized data set of users that use the app.

This project does not intend to replace any medical treatment or therapy.

# Installation

## From source code

### Backend
- Download the repository

- For the backend, python must be installed (I used version 3.10)

- Creating a python environment. Recommended to not install global libraries.
```
$ python3 -m venv venv
$ source venv/bin/activate
```

- Installing dependencies
```
$ pip install -r requirements.txt
```

- Execute the backend with:
```
python -m uvicorn main:app --reload
```

### Frontend
- For the frontend [NodeJS](https://nodejs.org/es/) and [npm](https://www.npmjs.com/) must be installed

```
$ sudo apt install nodejs npm -y
```
- As well as Vue [Vue](https://es.vuejs.org/)
```
$ npm install -g vue
```
- Install Vue dependencies.  
This will generate node_modules and package-lock.json
```
$ npm install
```

- Execute frontend with:
``` js
npm run devserve 
npm run proserve 
npm run devbuild 
npm run probuild 
```
dev* and pro* just changes the ip address of the server
Check the package.json scripts and Variables.js for more info.

## From production
This webapp is still not hosted

# Usage

Register or log in to the application to access the main page.
In the main page, you can see a list of Raynaud episodes that you have registered.
You can add, modify and delete Raynaud episodes.
When clicking on a Raynaud episode, you can see more information about it.
Access the "graphs" section to see statistics about the Raynaud episodes you have registered.
You can access the "studies" to se information about research studies or treatments.

# About the Author

I'm Alejandro, another freshly-baked developer.   
I still don't know what my specialty will be but i'm playing with all sort of technologies and I'm trying to learn new things.

This project is a possible solution for relatives and close friends who suffer from Raynaud and want to know more about it to keep it under control.

# Contribution
If for some unknown and unexpected reason you want to contribute, you can do it by pull requests, commenting and opening issues like in any other project.  
I will be veeeeeeeeeery excited to see your contribution.