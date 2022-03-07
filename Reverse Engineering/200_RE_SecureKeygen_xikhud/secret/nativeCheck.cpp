#include <jni.h>
#include <stdlib.h>
#include <string.h>
#include <android/log.h>

char* copyStringFromJString(JNIEnv* env, jstring s)
{
    const char* cs = env->GetStringUTFChars(s, NULL);
    char* ret = strdup(cs);
    env->ReleaseStringUTFChars(s, cs);
    return ret;
}

extern "C" JNIEXPORT jboolean JNICALL
Java_com_example_securekeygen_MainActivity_check(JNIEnv *env, jobject thiz, jstring name, jstring key)
{
    jboolean ret = JNI_FALSE;
    char* cname = copyStringFromJString(env, name);
    int nameLen = strlen(cname);
    char* ckey  = copyStringFromJString(env, key);
    char* ename = (char*)malloc(nameLen*2 + 1);
    char* hexename = (char*)malloc(nameLen*4+1);
    int i = 0;
    int j = nameLen - 1;
    for (; i < nameLen; ++i)
        ename[i] = cname[i];
    for (; i < nameLen*2; ++i, --j)
        ename[i] = cname[j];
    ename[i] = 0;
    //__android_log_write(ANDROID_LOG_DEBUG, "MyTag", ename);
    for (i = 0; i < nameLen*2; ++i)
    {
        sprintf(hexename+2*i, "%02x", (unsigned char)ename[i]);
    }
    hexename[4*nameLen] = 0;
    //__android_log_write(ANDROID_LOG_DEBUG, "MyTag", hexename);
    if (strcmp(hexename, ckey) == 0)
        ret = JNI_TRUE;
    free(hexename);
    free(ename);
    free(cname);
    free(ckey);
    return ret;
}