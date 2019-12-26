import { Component, OnInit, Input} from '@angular/core';
import { FormGroup, FormControl, FormBuilder } from '@angular/forms';
import { ApiService } from '../../api.service';

@Component({
  selector: 'app-order-form',
  templateUrl: './order-form.component.html',
  styleUrls: ['./order-form.component.css']
})
export class OrderFormComponent implements OnInit {

  @Input() products = [];
  @Input() cpus = [];
  @Input() motherboards = [];
  @Input() videocards = [];
  @Input() rammemorys = [];
  
  orderForm: FormGroup;

  constructor(
    
    private apiservice: ApiService
    
    ) {}

  ngOnInit() {
    this.orderForm = new FormGroup({
    name: new FormControl(null),
    cpu: new FormControl(null),
    motherboard: new FormControl(null),
    videocard: new FormControl(null),
    rammemory: new FormControl(null),
    rammemory2: new FormControl(null)
    });
  }
  saveForm(){
    console.log(this.orderForm.value);
    this.apiservice.createOrder(
      this.orderForm.value.name,
      this.orderForm.value.cpu, 
      this.orderForm.value.motherboard,
      this.orderForm.value.videocard, 
      this.orderForm.value.rammemory,
      this.orderForm.value.rammemory2
      ).subscribe(
        result => console.log(result),
        error => console.log(error)
    );
  }
}
