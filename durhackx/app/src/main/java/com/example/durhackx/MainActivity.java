package com.example.durhackx;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import okhttp3.Call;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.OkHttpClient;

import java.io.IOException;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        OkHttpClient client = new OkHttpClient();
        Button fire = (Button) findViewById(R.id.fireButton);
        Button left = (Button) findViewById(R.id.leftButton);
        Button right = (Button) findViewById(R.id.rightButton);

        left.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Request request = new Request.Builder()
                        .url("http://172.20.10.4/left")
                        .build();

                Call call = client.newCall(request);
                try {
                    Response response = call.execute();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }

            }

        });

        right.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Request request = new Request.Builder()
                        .url("172.20.10.4/right")
                        .build();

                Call call = client.newCall(request);
                try {
                    Response response = call.execute();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }

            }

        });

        fire.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Request request = new Request.Builder()
                        .url("172.20.10.4/fire")
                        .build();

                Call call = client.newCall(request);
                try {
                    Response response = call.execute();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }

            }

        });

    }
}