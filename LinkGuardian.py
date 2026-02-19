package com.s7.sentinel;

import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // ربط الزر من الواجهة
        Button guardButton = findViewById(R.id.guard_button);
        
        guardButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // تفعيل بروتوكول التحقق للسبع
                if (verifyAdmin("Alaa_Sabaa")) {
                    Toast.makeText(MainActivity.this, "🛡️ تم تفعيل نظام S7: الدخول آمن يا علاء", Toast.LENGTH_LONG).show();
                }
            }
        });
    }

    // وحدة التشفير الخاصة بـ S7-SENTINEL
    private String encryptPass(String password) {
        return Base64.encodeToString(password.getBytes(), Base64.DEFAULT);
    }

    // التحقق من الهوية الرقمية
    public boolean verifyAdmin(String input) {
        String adminKey = "QWxhYV9TYWJhYQ=="; // مفتاح السبع المشفر
        return encryptPass(input).trim().equals(adminKey.trim());
    }
}