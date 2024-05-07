import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UploadArticleComponent } from './upload-article/upload-article.component';


const routes: Routes = [
  { path: 'upload_article', component: UploadArticleComponent },
  { path: '', redirectTo: '/upload_article', pathMatch: 'full' },
  { path: '**', redirectTo: '/upload_article', pathMatch: 'full' } // Gérer les routes inconnues
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
