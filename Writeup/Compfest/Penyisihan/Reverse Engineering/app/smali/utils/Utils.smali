.class public abstract Lutils/Utils;
.super Ljava/lang/Object;
.source "Utils.java"


# direct methods
.method static constructor <clinit>()V
    .locals 0

    .line 12
    invoke-static {}, Lgo/Seq;->touch()V

    .line 13
    invoke-static {}, Lutils/Utils;->_init()V

    .line 14
    return-void
.end method

.method private constructor <init>()V
    .locals 0

    .line 16
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method private static native _init()V
.end method

.method public static native encrypt(Ljava/lang/String;)Ljava/lang/String;
.end method

.method public static native f()V
.end method

.method public static touch()V
    .locals 0

    .line 19
    return-void
.end method
