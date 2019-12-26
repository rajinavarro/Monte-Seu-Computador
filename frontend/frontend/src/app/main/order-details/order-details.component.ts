import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-order-details',
  templateUrl: './order-details.component.html',
  styleUrls: ['./order-details.component.css']
})
export class OrderDetailsComponent implements OnInit {
  
  @Input() order;
  @Output() selectProduct = new EventEmitter();
  constructor() { }

  ngOnInit() {}
  productClicked(product){
    this.selectProduct.emit(product);
  }
}
