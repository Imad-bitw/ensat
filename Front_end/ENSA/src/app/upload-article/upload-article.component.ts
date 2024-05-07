import { Component, ElementRef } from '@angular/core';
import { HttpClient, HttpEventType } from '@angular/common/http';
import { FormControl, FormGroup, Validators } from '@angular/forms';
@Component({
  selector: 'app-upload-article',
  templateUrl: './upload-article.component.html',
  styleUrls: ['./upload-article.component.css']
})
export class UploadArticleComponent {
 
  public verifyGroup!: FormGroup;
  resultat:any = null ;
  click_btn=false;
  questionText: string = '';
  constructor(private http: HttpClient) { }
  loading: boolean = false; // Ajoutez cette variable pour suivre l'état de chargement

    ngOnInit(): void {
    this.verifyGroup = new FormGroup({
      contrat_Fichier : new FormControl("", Validators.required)
    })
  }

  onFileSelected(event: any) {
    this.click_btn = true;
    this.resultat = null;
    this.loading = true; // Activez le chargement lors de l'envoi de la requête

    const file = event.target.files[0];
    const formData: FormData = new FormData();
    formData.append('file', file);

    this.http.post('http://localhost:8000/upload_article', formData)
      .subscribe(response => {
        if (response) {
          console.log(response);
          this.resultat = "Succées!"
          
        }
        this.loading = false; // Désactivez le chargement une fois la réponse reçue
      });
  }
  onSendQuestion() {
    // Vous pouvez traiter l'envoi de la question ici
    console.log("Question envoyée:", this.questionText);
    // Réinitialiser le champ de texte après l'envoi
    
    this.http.get(`http://localhost:8000/pose_question/${this.questionText}`)
    .subscribe(response => {
      if (response) {
        console.log(response);
        this.resultat = JSON.stringify(response)
        
      }
      this.loading = false; // Désactivez le chargement une fois la réponse reçue
    });
    
  }

  onClearDatabase() {
    // Logique pour vider la base de données
    this.http.get(`http://localhost:8000/clear_dbVector`)
    .subscribe(response => {
      if (response) {
        console.log(response);
        this.resultat = "Vide DB Succées!"
        
      }
      this.loading = false; // Désactivez le chargement une fois la réponse reçue
    });
  }

  onEmbadding() {
    // Logique pour Embadding
    console.log("Embadding !");
    this.http.get(`http://localhost:8000/embedding_db`)
    .subscribe(response => {
      if (response) {
        console.log(response);
        this.resultat = "Emedding Succées!"
        
      }
      this.loading = false; // Désactivez le chargement une fois la réponse reçue
    });
  }


}
