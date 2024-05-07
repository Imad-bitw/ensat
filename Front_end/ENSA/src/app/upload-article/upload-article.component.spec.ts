import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UploadArticleComponent } from './upload-article.component';

describe('UploadArticleComponent', () => {
  let component: UploadArticleComponent;
  let fixture: ComponentFixture<UploadArticleComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UploadArticleComponent]
    });
    fixture = TestBed.createComponent(UploadArticleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
