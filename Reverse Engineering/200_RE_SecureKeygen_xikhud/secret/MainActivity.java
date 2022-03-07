package com.example.securekeygen;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    static {
        System.loadLibrary("nativeCheck");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button checkButton = (Button)findViewById(R.id.checkButton);
        checkButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                EditText nameEditText = (EditText) findViewById(R.id.nameEditText);
                EditText keyEditText  = (EditText) findViewById(R.id.keyEditText);
                String name = nameEditText.getText().toString();
                String key  = keyEditText.getText().toString();
                boolean checkRet = check(name, key);
                if (checkRet == true) {
                    String msg = String.format("Nice, you have entered the correct key of \"%s\"", name);
                    Toast.makeText(getApplicationContext(), msg, Toast.LENGTH_SHORT).show();
                } else {
                    String msg = String.format("Wrong key for user \"%s\"", name);
                    Toast.makeText(getApplicationContext(), msg, Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    /**
     * A native method that is implemented by the 'easykeygen' native library,
     * which is packaged with this application.
     */
    public native boolean check(String name, String key);
}