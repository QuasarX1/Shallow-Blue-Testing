Imports System.Net
Imports System.IO
Imports System.Text
Imports Newtonsoft.Json

Module Functions

    Public Function serverRequest(sendData)

        Dim request As HttpWebRequest = DirectCast(WebRequest.Create("http://localhost:5555/test"), HttpWebRequest)

        request.Method = "POST"

        Dim dataStream As New StreamWriter(request.GetRequestStream())

        dataStream.Write(sendData)

        dataStream.Close()

        Dim responce As HttpWebResponse = DirectCast(request.GetResponse(), HttpWebResponse)

        Dim reader As StreamReader = New StreamReader(responce.GetResponseStream())

        Dim stringData As String = reader.ReadToEnd()

        reader.Close()

        Dim data = JSONConverter(stringData)

        Return data

    End Function

    Public Function JSONConverter(jsonData As String, Optional classType As String = vbNullString)

        'Example json data as a string [{"classType":"Temp","JSON_Text":"{'tempVar':'Hello'}"},{"classType":"Temp","JSON_Text":"{'tempVar':'World'}"}]

        Dim firstDeserialisation

        If classType = vbNullString Or classType = "JSON_Class_Extracter" Then

            firstDeserialisation = JsonConvert.DeserializeObject(Of JSON_Class_Extracter())(jsonData)

        ElseIf classType = "Text" Then

            Return JsonConvert.DeserializeObject(Of Text)(jsonData)

        Else

            firstDeserialisation = {}

            'error Class not recognised

            'Return New ClassNotRecognised()

        End If

        Dim deSerialisedData As New ArrayList

        For Each JSON_Object As JSON_Class_Extracter In firstDeserialisation

            deSerialisedData.Add(JSONConverter(JSON_Object.JSON_Text, JSON_Object.classType))

        Next

        Return deSerialisedData

    End Function

End Module
