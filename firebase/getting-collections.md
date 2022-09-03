
# Firestore functions

<br/>

> getting database

```javascript
const app = initializeApp(firebaseConfig)
const db = getFirestore(app)

```
<br/>

> getting root collection

```javascript
const collectionRef = collection(db, "collection_name")
```

<br/>

> getting all documents of a collection

```javascript
const getAllDocs = async()=>{
	const docsRef = await getDocs(collectionRef)
    docsRef.docs.map((docItem)=>{
        console.log(docItem.data())
    })
}
```

<br/>


> adding a document to collection

```javascript
// data should be an object
const data = {
    name:"omar",
    age:19
}
addDoc(collectionRef, data)
```

<br/>



> deleting a document in collection

```javascript
// data should be an object
const selcetedDocumentRef = doc(db, "collectionName", "theIdOfDocumnet")
deleteDoc(selcetedDocumentRef)
```

<br/>


> getting real time data from collection

```javascript
onSnapshot(collectionRef, (snapshot)=>{
    snapshot.docs.map((doc)=>{
        console.log(doc.data())
    })
})
```

<br/>


> getting spesific document from a collection

```javascript
const q = query(collectionRef, were("username", "==", "omar"))

```