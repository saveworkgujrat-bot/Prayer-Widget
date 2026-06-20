import os
import urllib.request

# Fix root build.gradle
with open("build.gradle", "w") as f:
    f.write("""buildscript {
    ext.kotlin_version = '1.9.10'
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:8.1.0'
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}
allprojects {
    repositories {
        google()
        mavenCentral()
    }
}
task clean(type: Delete) {
    delete rootProject.buildDir
}
""")

# Fix app/build.gradle
with open("app/build.gradle", "w") as f:
    f.write("""apply plugin: 'com.android.application'
apply plugin: 'kotlin-android'

android {
    namespace 'com.gujrat.prayerwidget'
    compileSdkVersion 34

    defaultConfig {
        applicationId "com.gujrat.prayerwidget"
        minSdkVersion 26
        targetSdkVersion 34
        versionCode 1
        versionName "1.0"
    }

    buildTypes {
        debug { minifyEnabled false }
    }

    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }

    kotlinOptions {
        jvmTarget = '1.8'
    }
}

dependencies {
    implementation 'androidx.core:core-ktx:1.12.0'
}
""")

# Create gradle wrapper properties
os.makedirs("gradle/wrapper", exist_ok=True)
with open("gradle/wrapper/gradle-wrapper.properties", "w") as f:
    f.write("""distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.1.1-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
""")

# Download gradlew script
url = "https://raw.githubusercontent.com/gradle/gradle/v8.1.1/gradlew"
urllib.request.urlretrieve(url, "gradlew")
os.chmod("gradlew", 0o755)

print("Build files fixed successfully!")
