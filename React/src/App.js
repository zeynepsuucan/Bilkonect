import './App.css';
import EntryPage from './EntryPage/EntryPage.jsx';
import LoginPage from './LoginPage/LoginPage.jsx';
import SignupPage from './SignupPage/SignupPage.jsx';

import SearchChoosePage from './SearchChoosePage/SearchChoosePage.jsx';
import SearchPostsPage from './SearchPostsPage/SearchPostsPage.jsx';
import SearchProfilesPage from './SearchProfilesPage/SearchProfilesPage.jsx';
import EditProfilePage from './EditProfilePage/EditProfilePage.jsx';

import PostsPage from './PostsPage/PostsPage.jsx';
import HomePage from './HomePage/HomePage.jsx';

import RecoveryPage from './RecoveryPage/RecoveryPage.jsx';
import LeftBar from './SideBarComponents/LeftBar.jsx';

import ProfilePage from './ProfilePage/ProfilePage.jsx';
import OwnProfilePage from './OwnProfilePage/OwnProfilePage.jsx';

import {BrowserRouter, Route, Routes} from "react-router-dom";

import CreatePostPage from './CreatePostPage/CreatePostPage.jsx';
import CreateChoosePage from './CreateChoosePage/CreateChoosePage.jsx';
import PostReviewPage from './PostReviewPage/PostReviewPage.jsx';

import MiniProfile from './SearchProfilesPage/MiniProfile.jsx'; 
import ChatBox from './ChatComponents/ChatBox.jsx';
import ChatPrev from './ChatComponents/ChatPrev.jsx';
import ChatPage from './ChatPage/ChatPage.jsx';

import ChatAccessPage from './ChatAccessPage/ChatAccessPage.jsx'
import StudentPage from './StudentPage/StudentPage.jsx';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<EntryPage/>}/>
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/signup" element={<SignupPage/>}/>
        <Route path="/postspage" element={<PostsPage/>}/>
        <Route path="/createChoosePage" element={<CreateChoosePage/>}/>
        <Route path="/createPostPage/:postType" element={<CreatePostPage/>}/>
        <Route path="/postreview/:post_id" element={<PostReviewPage/>}/>

        <Route path="/chats/:chat_id" element={<ChatPage/>}/>
        <Route path="/chatsAccess" element={<ChatAccessPage/>}/>

        <Route path="/ownProfile" element={<OwnProfilePage/>}/>
        <Route path="/searchPage" element={<SearchChoosePage/>}/>
        <Route path="/searchPosts" element={<SearchPostsPage/>}/>
        <Route path="/searchProfiles" element={<SearchProfilesPage/>}/>
        <Route path="/visitProfile/:username" element={<ProfilePage/>}/>

        <Route path="/editOwnProfile" element={<EditProfilePage/>}/>
        <Route path="/studentPage" element={<StudentPage/>}/>

        <Route path="/accrecovery" element={<RecoveryPage/>}/>
      </Routes>
      </BrowserRouter>

      
      
    </div>
  );
}

export default App;
