import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {Routes, RouterModule} from '@angular/router';
import { ProductsComponent } from './products.component';
import { ApiService } from '../api.service';
import {ProductDetailsComponent } from './product-details/product-details.component';
import {ProductListComponent} from './product-list/product-list.component';

const routes: Routes = [
  {path: 'products', component: ProductsComponent}
];

@NgModule({
  declarations: [
    ProductsComponent,
    ProductListComponent,
    ProductDetailsComponent
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(routes)
  ],
  exports: [
    RouterModule
  ],
  providers:[
    ApiService
  ]
})
export class ProductsModule { }
