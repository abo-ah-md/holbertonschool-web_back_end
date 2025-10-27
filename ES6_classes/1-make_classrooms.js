import ClassRoom from "./0-classroom";

function initializeRooms (){
const newclass1 = new ClassRoom(19);
const newclass2 = new ClassRoom(20);
const newclass3 = new ClassRoom(34);
return [
    newclass1._maxStudentsSize,
    newclass2._maxStudentsSize,
    newclass3._maxStudentsSize
]
}