import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseUrl ='http://127.0.0.1:8000/';
  headers = new HttpHeaders({
    'Content-Type': 'application/json'
  });

  constructor(
    private httpClient: HttpClient
  ) { }

 
 getCpus(){
    return this.httpClient.get(this.baseUrl+'products/api/cpu',
    {headers: this.headers});
  }
  getMotherboards(){
    return this.httpClient.get(this.baseUrl+'products/api/motherboard',
    {headers: this.headers});
  }
  getVideocards(){
    return this.httpClient.get(this.baseUrl+'products/api/video-card',
    {headers: this.headers});
  }
  getRammemorys(){
    return this.httpClient.get(this.baseUrl+'products/api/ram-memory',
    {headers: this.headers});
  }
  getProducts(){
    return this.httpClient.get(this.baseUrl+'products/api/',
    {headers: this.headers});
  }
  getOrders(){
     
    return this.httpClient.get(this.baseUrl+'orders/api/', {headers: this.headers});
  }
  createOrder(name: string, cpu: string, motherboard: string, videocard:string, rammemory:string, rammemory2: string){
    console.log(this.headers);
    const body = JSON.stringify({name, cpu, motherboard, videocard, rammemory, rammemory2});
    
    return this.httpClient.post(this.baseUrl+'orders/api/',body,{headers: this.headers});
  }
}