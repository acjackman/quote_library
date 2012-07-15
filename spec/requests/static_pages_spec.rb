require 'spec_helper'

describe "Static pages" do

  describe "Home page" do

    it "should have the content 'Quote'" do
      visit '/static_pages/home'
      page.should have_content('Quote')
    end
  end
  
  describe  "Help page" do
    
    it "should have the content 'Help'" do
      visit '/static_pages/help'
      page.should have_content('Help')
    end
  end
  
  describe "About page" do
    
    it "should have the content 'About this site'" do
      visit '/static_pages/about'
      page.should have_content('About this site')
    end
  end
end