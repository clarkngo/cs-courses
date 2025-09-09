function Profile() {
    return (
        <img
            src="./katherine-johnson.png"
            alt="Katherine Johnson"
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
