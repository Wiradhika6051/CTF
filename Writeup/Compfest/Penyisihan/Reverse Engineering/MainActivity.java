public class com.ivanox.godroid.MainActivity extends androidx.appcompat.app.AppCompatActivity {
	 /* .source "MainActivity.java" */
	 /* # direct methods */
	 public com.ivanox.godroid.MainActivity ( ) {
		 /* .locals 0 */
		 /* .line 10 */
		 /* invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V */
		 return;
	 } // .end method
	 /* # virtual methods */
	 protected void onCreate ( android.os.Bundle p0 ) {
		 /* .locals 1 */
		 /* .param p1, "savedInstanceState" # Landroid/os/Bundle; */
		 /* .line 13 */
		 /* invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V */
		 /* .line 14 */
		 /* const v0, 0x7f0b001c */
		 (( com.ivanox.godroid.MainActivity ) p0 ).setContentView ( v0 ); // invoke-virtual {p0, v0}, Lcom/ivanox/godroid/MainActivity;->setContentView(I)V
		 /* .line 15 */
		 return;
	 } // .end method
	 public void onSubmit ( android.view.View p0 ) {
		 /* .locals 4 */
		 /* .param p1, "v" # Landroid/view/View; */
		 /* .line 18 */
		 /* const v0, 0x7f0800ac */
		 (( com.ivanox.godroid.MainActivity ) p0 ).findViewById ( v0 ); // invoke-virtual {p0, v0}, Lcom/ivanox/godroid/MainActivity;->findViewById(I)Landroid/view/View;
		 /* check-cast v0, Landroid/widget/EditText; */
		 (( android.widget.EditText ) v0 ).getText ( ); // invoke-virtual {v0}, Landroid/widget/EditText;->getText()Landroid/text/Editable;
		 (( java.lang.Object ) v0 ).toString ( ); // invoke-virtual {v0}, Ljava/lang/Object;->toString()Ljava/lang/String;
		 /* .line 20 */
		 /* .local v0, "licenseKey":Ljava/lang/String; */
		 utils.Utils .encrypt ( v0 );
		 final String v2 = "650e2014a6d7041d8024a8984e47cc9810cead06b0c24dfc742aa71c6de29cb42679b1544286ed09cbf2d2bebd7c2ccd1148"; // const-string v2, "650e2014a6d7041d8024a8984e47cc9810cead06b0c24dfc742aa71c6de29cb42679b1544286ed09cbf2d2bebd7c2ccd1148"
		 v1 = 		 (( java.lang.String ) v1 ).equals ( v2 ); // invoke-virtual {v1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
		 /* const v2, 0x7f0801af */
		 if ( v1 != null) { // if-eqz v1, :cond_0
			 /* .line 21 */
			 (( com.ivanox.godroid.MainActivity ) p0 ).findViewById ( v2 ); // invoke-virtual {p0, v2}, Lcom/ivanox/godroid/MainActivity;->findViewById(I)Landroid/view/View;
			 /* check-cast v1, Landroid/widget/TextView; */
			 int v2 = 1; // const/4 v2, 0x1
			 /* new-array v2, v2, [Ljava/lang/Object; */
			 int v3 = 0; // const/4 v3, 0x0
			 /* aput-object v0, v2, v3 */
			 final String v3 = "Correct! Here\'s your Flag: COMPFEST15{%s}"; // const-string v3, "Correct! Here\'s your Flag: COMPFEST15{%s}"
			 java.lang.String .format ( v3,v2 );
			 (( android.widget.TextView ) v1 ).setText ( v2 ); // invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
			 /* .line 23 */
		 } // :cond_0
		 (( com.ivanox.godroid.MainActivity ) p0 ).findViewById ( v2 ); // invoke-virtual {p0, v2}, Lcom/ivanox/godroid/MainActivity;->findViewById(I)Landroid/view/View;
		 /* check-cast v1, Landroid/widget/TextView; */
		 final String v2 = "Wrong!"; // const-string v2, "Wrong!"
		 (( android.widget.TextView ) v1 ).setText ( v2 ); // invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
		 /* .line 25 */
	 } // :goto_0
	 return;
} // .end method
