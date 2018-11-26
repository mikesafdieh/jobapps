import axios from 'axios';
import AuthService from '../auth/AuthService';

const BASE_URL = 'http://localhost:8000/api';


export class APIService{
    constructor(){

    }

    // get all jobapps
    getJobApps() {
        const url = `${BASE_URL}/jobapps/`;
        const headers = { Authorization: `Bearer ${AuthService.getAuthToken()}`};
        return axios.get(url, {'headers': headers}).then(response => response.data);
    }

    // get one jobapp
    getJobApp(pk) {
    	const url = `${BASE_URL}/jobapps/${pk}`;
    	const headers = { Authorization: `Bearer ${AuthService.getAuthToken()}`};
    	return axios.get(url, {'headers': headers}).then(response => response.data);
    }
}