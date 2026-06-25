import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;


class Homepage extends StatefulWidget{
  const Homepage({super.key});
@override
  State<Homepage> createState(){
   return _HomePageState(); 
  }
  }
  class _HomePageState extends State<Homepage> {

  File? imageFile;

  String prediction = "";

  Future<void> takePhoto() async {

    final picker = ImagePicker();

    final XFile? image = await picker.pickImage(
      source: ImageSource.camera,
    );

    if (image != null) {
      setState(() {
        imageFile = File(image.path);
      });
    }
  }

  Future<void> predictDigit() async {

    if (imageFile == null) return;

    var request = http.MultipartRequest(
      'POST',
      Uri.parse(
        'http://192.168.31.231:8000/predict',
      ),
    );

    request.files.add(
      await http.MultipartFile.fromPath(
        'file',
        imageFile!.path,
      ),
    );

    var response = await request.send();

    var body =
        await response.stream.bytesToString();

    var data = jsonDecode(body);

    setState(() {
      prediction =
          data["digit"].toString();
    });
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(

      appBar: AppBar(
        title: const Text(
          "Digit Recognizer",
        ),
      ),

      body: Padding(
        padding: const EdgeInsets.all(20),

        child: Column(

          children: [

            const SizedBox(height: 20),

            imageFile == null
                ? const Text("No Image Selected")
                : Image.file(
                    imageFile!,
                    height: 250,
                  ),

            const SizedBox(height: 20),

            ElevatedButton(
              onPressed: takePhoto,
              child: const Text(
                "Take Photo",
              ),
            ),

            const SizedBox(height: 20),

            ElevatedButton(
              onPressed: predictDigit,
              child: const Text(
                "Predict",
              ),
            ),

            const SizedBox(height: 30),

            Text(
              "Prediction: $prediction",
              style: const TextStyle(
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

