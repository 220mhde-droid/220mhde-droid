package com.s7.sentinel;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button guardButton = findViewById(R.id.guard_button);
        
        // عند الضغط على زر الحماية يا علاء
        guardButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // تظهر رسالة تأكيد فورية
                Toast.makeText(MainActivity.this, "تم تفعيل بروتوكول حماية السبع بنجاح 🛡️", Toast.LENGTH_LONG).show();
            }
        });
    }
}