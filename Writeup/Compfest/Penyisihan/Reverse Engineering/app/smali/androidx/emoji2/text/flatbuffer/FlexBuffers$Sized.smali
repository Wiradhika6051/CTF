.class abstract Landroidx/emoji2/text/flatbuffer/FlexBuffers$Sized;
.super Landroidx/emoji2/text/flatbuffer/FlexBuffers$Object;
.source "FlexBuffers.java"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Landroidx/emoji2/text/flatbuffer/FlexBuffers;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x40a
    name = "Sized"
.end annotation


# instance fields
.field protected final size:I


# direct methods
.method constructor <init>(Landroidx/emoji2/text/flatbuffer/ReadBuf;II)V
    .locals 2
    .param p1, "buff"    # Landroidx/emoji2/text/flatbuffer/ReadBuf;
    .param p2, "end"    # I
    .param p3, "byteWidth"    # I

    .line 657
    invoke-direct {p0, p1, p2, p3}, Landroidx/emoji2/text/flatbuffer/FlexBuffers$Object;-><init>(Landroidx/emoji2/text/flatbuffer/ReadBuf;II)V

    .line 658
    iget-object v0, p0, Landroidx/emoji2/text/flatbuffer/FlexBuffers$Sized;->bb:Landroidx/emoji2/text/flatbuffer/ReadBuf;

    sub-int v1, p2, p3

    invoke-static {v0, v1, p3}, Landroidx/emoji2/text/flatbuffer/FlexBuffers;->access$100(Landroidx/emoji2/text/flatbuffer/ReadBuf;II)I

    move-result v0

    iput v0, p0, Landroidx/emoji2/text/flatbuffer/FlexBuffers$Sized;->size:I

    .line 659
    return-void
.end method


# virtual methods
.method public size()I
    .locals 1

    .line 662
    iget v0, p0, Landroidx/emoji2/text/flatbuffer/FlexBuffers$Sized;->size:I

    return v0
.end method
