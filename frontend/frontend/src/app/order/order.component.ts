import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {
  products: any = [];
  cpus: any = [];
  motherboards: any = [];
  videocards: any = [];
  rammemorys: any = [];
  

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
}
