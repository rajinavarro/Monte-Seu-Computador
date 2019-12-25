import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class OrderService {

  orderUrl = 'http://127.0.0.1:8000/orders/api/'

  constructor(private http: HttpClient) { }

  list() {
    return this.http.get<any[]>(`${this.orderUrl}`);

  }
}
