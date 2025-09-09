import profile from "./profile.png";
export function Profile() {
    return (
        <img
            src={profile}
            alt="Profile Picture"
        />
    );
}
  
export default function Gallery() {
    return (
        <section>
            <h1>Amazing scientists</h1>
            <Profile />
            <Profile />
            <Profile />
        </section>
    );
}
