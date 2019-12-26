import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  orders: any = [];
  products: any = [];
  cpus: any = [];
  motherboards: any = [];
  videocards: any = [];
  rammemorys: any = [];
  selectedOrder = null;
  selectedProduct = null;

  constructor(
    private apiservice: ApiService
    ) { }

  ngOnInit() {


    this.apiservice.getCpus().subscribe(
      data => {
        this.cpus = data;
      },
      error => console.log(error)
    );
    this.apiservice.getRammemorys().subscribe(
      data => {
        this.rammemorys = data;
      },
      error => console.log(error)
    );
    this.apiservice.getMotherboards().subscribe(
      data => {
        this.motherboards = data;
      },
      error => console.log(error)
    );
    
    this.apiservice.getVideocards().subscribe(
      data => {
        this.videocards = data;
      },
      error => console.log(error)
    );
    
   
    this.apiservice.getOrders().subscribe(
      data => {
        this.orders = data;
      },
      error => console.log(error)
    );
  }

  selectProduct(product){
    this.selectedProduct = product;
    console.log('selectedProduct', this.selectProduct);
  }
  selectOrder(order){
    this.selectedOrder = order;
    console.log('selectedOrder', this.selectedOrder);
  }

}
