.class public Lcom/ivanox/godroid/MainActivity;
.super Landroidx/appcompat/app/AppCompatActivity;
.source "MainActivity.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 10
    invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V

    return-void
.end method


# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 1
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .line 13
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 14
    const v0, 0x7f0b001c

    invoke-virtual {p0, v0}, Lcom/ivanox/godroid/MainActivity;->setContentView(I)V

    .line 15
    return-void
.end method

.method public onSubmit(Landroid/view/View;)V
    .locals 4
    .param p1, "v"    # Landroid/view/View;

    .line 18
    const v0, 0x7f0800ac

    invoke-virtual {p0, v0}, Lcom/ivanox/godroid/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/EditText;

    invoke-virtual {v0}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v0

    .line 20
    .local v0, "licenseKey":Ljava/lang/String;
    invoke-static {v0}, Lutils/Utils;->encrypt(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    const-string v2, "650e2014a6d7041d8024a8984e47cc9810cead06b0c24dfc742aa71c6de29cb42679b1544286ed09cbf2d2bebd7c2ccd1148"

    invoke-virtual {v1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    const v2, 0x7f0801af

    if-eqz v1, :cond_0

    .line 21
    invoke-virtual {p0, v2}, Lcom/ivanox/godroid/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/TextView;

    const/4 v2, 0x1

    new-array v2, v2, [Ljava/lang/Object;

    const/4 v3, 0x0

    aput-object v0, v2, v3

    const-string v3, "Correct! Here\'s your Flag: COMPFEST15{%s}"

    invoke-static {v3, v2}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    goto :goto_0

    .line 23
    :cond_0
    invoke-virtual {p0, v2}, Lcom/ivanox/godroid/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/TextView;

    const-string v2, "Wrong!"

    invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 25
    :goto_0
    return-void
.end method
