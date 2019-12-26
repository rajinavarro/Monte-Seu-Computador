import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-order-list',
  templateUrl: './order-list.component.html',
  styleUrls: ['./order-list.component.css']
})
export class OrderListComponent implements OnInit {
  
  @Input() orders = [];
  @Output() selectOrder = new EventEmitter();
  
  constructor() { }

  ngOnInit() {}
  orderClicked(order){
    this.selectOrder.emit(order);
  }
}
