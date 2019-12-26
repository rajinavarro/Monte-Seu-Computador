import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {
  products: any = [];
  cpus: any = [];
  motherboards: any = [];
  videocards: any = [];
  rammemorys: any = [];
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
    

  }

  selectProduct(product){
    this.selectedProduct = product;
    console.log('selectedProduct', this.selectProduct);
  }

}

